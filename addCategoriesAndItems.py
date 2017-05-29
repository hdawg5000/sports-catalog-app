from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import User, Category, Item, Base

engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#Create admin user
adminUser = User(name="Hammad Naseem", username="Admin")
session.add(adminUser)
session.commit()

#Query the just created admin user
admin = session.query(User).filter_by(username="Admin").one()

#Create basketball category
basketballCategory = Category(name="Basketball")
session.add(basketballCategory)
session.commit()

#Create items for the basketball category
category = session.query(Category).filter_by(name="Basketball").one()

item1 = Item(name="Basketball Shoes",
    description="Proper basketball shoes are recommended for proper traction,\
     ankle support as well as comfort while playing",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Athletic Socks",
    description="Wear two pairs of athletic socks to prevent blisters while\
     giving added comfort",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item3 = Item(name="Athletic Shorts",
    description="Wear loose-fitted pair of shorts that are comofrtable to move\
     around in",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item4 = Item(name="Mouth Guard",
    description="Wear a mouth guard to protect your mouth area, especially your\
     teeth, from accidental contact by other players",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item5 = Item(name="Basketball",
    description="There are different sized backsetball for each gender as well\
     as age group. Select a ball that has good grip and is properly inflated",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item6 = Item(name="Basketball Hoop",
    description="Basketball hoops are necessary to play the game of basketball.\
     Offical hoops stand 10ft tall and have either a stringed net or chained",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

#Create football category
footballCategory = Category(name="Football")
session.add(footballCategory)
session.commit()

#Create items for the football category
category = session.query(Category).filter_by(name="Football").one()

item1 = Item(name="Cleats",
    description="Football is played on the grass so for proper traction, cleats\
     should be worn. However, causal gameplay can be played with regular shoes",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Athletic Socks", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item3 = Item(name="Athletic Shorts", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item4 = Item(name="Mouth Guard",
    description="Wear a mouth guard to protect your mouth area, especially your\
     teeth as this is a physical contact sport", 
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item5 = Item(name="Football",
    description="This is the ball required to play the game. There are different\
     sizes depending on age. Choose the one within your age range and one that\
     comofortably fits around your hand.",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item6 = Item(name="Football Helmet",
    description="A helmet is the most important equipment piece for football as \
     there is a lot of contact in this game. The helmet should be comfortable \
     and secure around your head.",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item6 = Item(name="Football Pads", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

#Create baseball category
baseballCategory = Category(name="Baseball")
session.add(basketballCategory)
session.commit()

#Create items for the baseball category
category = session.query(Category).filter_by(name="Basketball").one()

item1 = Item(name="Basketball Shoes", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Athletic Socks", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item3 = Item(name="Athletic Shorts", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item4 = Item(name="Mouth Guard", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item5 = Item(name="Basketball", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item6 = Item(name="Basketball Hoop", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

#Create badminton category
badmintonCategory = Category(name="Badminton")
session.add(badmintonCategory)
session.commit()

#Create items for the badminton category
category = session.query(Category).filter_by(name="Basketball").one()

item1 = Item(name="Basketball Shoes", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Athletic Socks", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item3 = Item(name="Athletic Shorts", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item4 = Item(name="Mouth Guard", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item5 = Item(name="Basketball", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item6 = Item(name="Basketball Hoop", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

#Create soccer category
soccerCategory = Category(name="Soccer")
session.add(soccerCategory)
session.commit()

#Create items for the soccer category
category = session.query(Category).filter_by(name="Basketball").one()

item1 = Item(name="Basketball Shoes", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Athletic Socks", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item3 = Item(name="Athletic Shorts", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item4 = Item(name="Mouth Guard", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item5 = Item(name="Basketball", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item6 = Item(name="Basketball Hoop", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

#Create tennis category
tennisCategory = Category(name="Tennis")
session.add(tennisCategory)
session.commit()

#Create items for the tennis category
category = session.query(Category).filter_by(name="Basketball").one()

item1 = Item(name="Basketball Shoes", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Athletic Socks", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item3 = Item(name="Athletic Shorts", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item4 = Item(name="Mouth Guard", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item5 = Item(name="Basketball", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item6 = Item(name="Basketball Hoop", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

#Create hockey category
hockeyCategory = Category(name="Hockey")
session.add(hockeyCategory)
session.commit()

#Create items for the hockey category
category = session.query(Category).filter_by(name="Basketball").one()

item1 = Item(name="Basketball Shoes", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Athletic Socks", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item3 = Item(name="Athletic Shorts", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item4 = Item(name="Mouth Guard", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item5 = Item(name="Basketball", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item6 = Item(name="Basketball Hoop", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

#Create golf category
golfCategory = Category(name="Golf")
session.add(golfCategory)
session.commit()

#Create items for the golf category
category = session.query(Category).filter_by(name="Basketball").one()

item1 = Item(name="Basketball Shoes", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Athletic Socks", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item3 = Item(name="Athletic Shorts", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item4 = Item(name="Mouth Guard", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item5 = Item(name="Basketball", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item6 = Item(name="Basketball Hoop", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

#Create volleyball category
volleyballCategory = Category(name="Volleyball")
session.add(volleyballCategory)
session.commit()

#Create items for the volleyball category
category = session.query(Category).filter_by(name="Basketball").one()

item1 = Item(name="Basketball Shoes", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Athletic Socks", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item3 = Item(name="Athletic Shorts", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item4 = Item(name="Mouth Guard", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item5 = Item(name="Basketball", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item6 = Item(name="Basketball Hoop", description="Shoes needed", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()
