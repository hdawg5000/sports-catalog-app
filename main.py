from flask import Flask, render_template, request, url_for, redirect, jsonify, make_response
from database_setup import Base, Category, Item, User
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, desc
from flask import session as login_session
import json, random, string, httplib2, requests
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

@app.route('/gconnect', methods=['POST'])
def gconnect():
    #Check token client sends to server matches token server sends to client
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    code = request.data

    try:
        #Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    #Check if user is an existing user in the databse. If not, add to database
    user = session.query(User).filter_by(username=login_session['email']).one_or_none()

    #If user doesn't exist, create new user
    if user is None:
        newUser = User(name=login_session['username'], username=login_session['email'])
        session.add(newUser)
        session.commit()

    return redirect(url_for('showHomePage'))

#Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    credentials = login_session['credentials']
    access_token = credentials.access_token
    #Only disconnect a connected user
    if access_token is None:
        response = make_response(json.dumps('Current user not connected', 401))
        response.headers['Content-Type'] = 'application/json'
        return response

    #Execute HTTP GET request to revoke current token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    #If response is 200, token was successfully revoked
    if result['status'] == '200':
        #Reset user's session
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected'), 200)
        response.headers['Content-Type'] = 'application/json'
        return redirect(url_for('showHomePage'))
    else:
        #Any response other than 200, the given token was Invalid
        response = make_response(json.dumps('Failed to revoke token for given user', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

#Show all categories and last 8 items by updated_at timestamp
@app.route('/')
def showHomePage():
    #Check is user is logged in. If not, add item link will be hidden
    logged_in = True
    if 'username' not in login_session:
        logged_in = False
    categories = session.query(Category).all()
    latestItems = session.query(Item).order_by(desc(Item.updated_at)).limit(8)
    return render_template('index.html', categories=categories, latestItems=latestItems, allowed=logged_in)

#Show all items in a category when clicking on the category
@app.route('/category/<int:category_id>/items')
def showItems(category_id):
    #Check is user is logged in. If not, add item link will be hidden
    logged_in = True
    if 'username' not in login_session:
        logged_in = False
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    return render_template('showItems.html', items=items, category=category, categories=categories, allowed=logged_in)

#Show item name and description
@app.route('/category/<int:category_id>/item/<int:item_id>')
def showItem(category_id, item_id):
    #Check is user is logged in. If not, edit and delete links will be hidden
    logged_in = True
    if 'username' not in login_session:
        logged_in = False
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('showItem.html', item=item, category=category, allowed=logged_in)

#Add a new item given the category ID
@app.route('/item/new', methods=['GET', 'POST'])
def addItem():
    logged_in = True
    categories = session.query(Category).all()
    if request.method == 'POST':
        #Check is user is logged in. If not, redirect to login page
        if 'username' not in login_session:
            logged_in = False
            return redirect('/login')
        else:
            categoryName = request.form['category']
            category = session.query(Category).filter_by(name=categoryName).one()
            newItem = Item(name=request.form['name'], description=request.form['description'], category_id=category.id, user_id=1)
            session.add(newItem)
            session.commit()
            return redirect(url_for('showItems', category_id=category.id))
    else:
        return render_template('addItem.html', categories=categories, allowed=logged_in)

#Edit an item given the category ID
@app.route('/category/<int:category_id>/item/<int:item_id>/edit', methods=['GET', 'POST'])
def editItem(category_id, item_id):
    logged_in = True
    if request.method == 'POST':
        #Check is user is logged in. If not, redirect to login page
        if 'username' not in login_session:
            return redirect('/login')
        else:
            category = session.query(Category).filter_by(name=request.form['category']).one()
            item = session.query(Item).filter_by(id=item_id).one()
            item.name = request.form['name']
            item.description = request.form['description']
            item.category_id = category.id
            session.add(item)
            session.commit()
            return redirect(url_for('showItems', category_id=category.id))
    else:
        category = session.query(Category).filter_by(id=category_id).one()
        item = session.query(Item).filter_by(id=item_id).one()
        categories = session.query(Category).all()
        user_id = item.user_id
        item_creator = session.query(User).filter_by()
        return render_template('editItem.html', item=item, category=category, categories=categories, allowed=logged_in)

#Delete item from category
@app.route('/category/<int:category_id>/item/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    #Check is user is logged in. If not, redirect to login page
    logged_in = True
    if 'username' not in login_session:
        logged_in = False
        return redirect('/login')
    else:
        category = session.query(Category).filter_by(id=category_id).one()
        if request.method == 'POST':
            item = session.query(Item).filter_by(id=item_id).one()
            session.delete(item)
            session.commit()
            return redirect(url_for('showItems', category_id=category.id, allowed=logged_in))
        else:
            item = session.query(Item).filter_by(id=item_id).one()
            return render_template('deleteItem.html', item=item, category=category, allowed=logged_in)

#API endpoint to show all categories
@app.route('/api/v1/categories.json')
def showAllCategoriesJSON():
    categories = session.query(Category).all()
    return jsonify(Categories = [i.serialize for i in categories])

#API endpoint to show all items
@app.route('/api/v1/items.json')
def showAllItemsJSON():
    items = session.query(Item).all()
    return jsonify(Items = [i.serialize for i in items])

#API endpoint to show all items in a given category
@app.route('/api/v1/category/<int:category_id>/items.json')
def showItemsJSON(category_id):
    items = session.query(Item).filter_by(category_id=category_id).all()
    return jsonify(Items = [i.serialize for i in items])

#API endpoint to show category given category ID
@app.route('/api/v1/category/<int:category_id>.json')
def showCategoryJSON(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    return jsonify(Category = category.serialize)

#API endpoint to show item given item ID
@app.route('/api/v1/item/<int:item_id>.json')
def showItemJSON(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return jsonify(Item = item.serialize)

#API endpoint to show all users
@app.route('/api/v1/users.json')
def showAllUsersJSON():
    users = session.query(User).all()
    return jsonify(Users = [i.serialize for i in users])

#API endpoint to show user information
@app.route('/api/v1/user/<int:user_id>.json')
def showUserJSON(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return jsonify(Users = user.serialize)

if __name__ == '__main__':
    app.secret_key = 'secret'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
