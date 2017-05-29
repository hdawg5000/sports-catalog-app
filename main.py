from flask import Flask, render_template, request, url_for, redirect, jsonify
from database_setup import Base, Category, Item, User
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, desc
import json

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

#Show all categories and last 8 items by updated_at timestamp
@app.route('/')
def showHomePage():
    categories = session.query(Category).all()
    latestItems = session.query(Item).order_by(desc(Item.updated_at)).limit(8)
    return render_template('index.html', categories=categories, latestItems=latestItems)

#Show all items in a category when clicking on the category
@app.route('/category/<int:category_id>/items')
def showItems(category_id):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    return render_template('showItems.html', items=items, category=category, categories=categories)

#Show item name and description
@app.route('/category/<int:category_id>/item/<int:item_id>')
def showItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('showItem.html', item=item, category=category)

#Add a new item given the category ID
@app.route('/item/new', methods=['GET', 'POST'])
def addItem():
    categories = session.query(Category).all()
    if request.method == 'POST':
        categoryName = request.form['category']
        category = session.query(Category).filter_by(name=categoryName).one()
        newItem = Item(name=request.form['name'], description=request.form['description'], category_id=category.id, user_id=1)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showItems', category_id=category.id))
    else:
        return render_template('addItem.html', categories=categories)

#Edit an item given the category ID
@app.route('/category/<int:category_id>/item/<int:item_id>/edit', methods=['GET', 'POST'])
def editItem(category_id, item_id):
    if request.method == 'POST':
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
        return render_template('editItem.html', item=item, category=category, categories=categories)

#Delete item from category
@app.route('/category/<int:category_id>/item/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        item = session.query(Item).filter_by(id=item_id).one()
        session.delete(item)
        session.commit()
        return redirect(url_for('showItems', category_id=category.id))
    else:
        item = session.query(Item).filter_by(id=item_id).one()
        return render_template('deleteItem.html', item=item, category=category)

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
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
