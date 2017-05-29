from flask import Flask, render_template, request, url_for
from database_setup import Base, Category, Item, User
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, desc

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
    return render_template('index.html', categories=categories, \
        latestItems=latestItems)

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
    #category = session.query(Category).filter_by(id=category_id).one()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('showItem.html', item=item)

#Add a new item given the category ID
@app.route('/item/new', methods=['GET', 'POST'])
def addItem():
    categories = session.query(Category).all()
    return render_template('addItem.html', categories=categories)

#Edit an item given the category ID
@app.route('/category/<int:category_id>/item/<int:item_id>/edit', methods=['GET', 'POST'])
def editItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    categories = session.query(Category).all()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('editItem.html', item=item, category=category, categories=categories)

#Delete item from category
@app.route('/category/<int:category_id>/item/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    categories = session.query(Category).all()
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('deleteItem.html', item=item, category=category)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
