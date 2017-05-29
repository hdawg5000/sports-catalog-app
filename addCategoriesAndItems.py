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
session.add(item2)
session.commit()

item3 = Item(name="Athletic Shorts",
    description="Wear loose-fitted pair of shorts that are comofrtable to move\
     around in",
    category_id=category.id, user_id=admin.id)
session.add(item3)
session.commit()

item4 = Item(name="Mouth Guard",
    description="Wear a mouth guard to protect your mouth area, especially your\
     teeth, from accidental contact by other players",
    category_id=category.id, user_id=admin.id)
session.add(item4)
session.commit()

item5 = Item(name="Basketball",
    description="There are different sized backsetball for each gender as well\
     as age group. Select a ball that has good grip and is properly inflated",
    category_id=category.id, user_id=admin.id)
session.add(item5)
session.commit()

item6 = Item(name="Basketball Hoop",
    description="Basketball hoops are necessary to play the game of basketball.\
     Offical hoops stand 10ft tall and have either a stringed net or chained",
    category_id=category.id, user_id=admin.id)
session.add(item6)
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

item2 = Item(name="Mouth Guard",
    description="Wear a mouth guard to protect your mouth area, especially your\
     teeth as this is a physical contact sport.",
    category_id=category.id, user_id=admin.id)
session.add(item2)
session.commit()

item3 = Item(name="Football",
    description="This is the ball required to play the game. There are different\
     sizes depending on age. Choose the one within your age range and one that\
     comofortably fits around your hand.",
    category_id=category.id, user_id=admin.id)
session.add(item3)
session.commit()

item4 = Item(name="Football Helmet",
    description="A helmet is the most important equipment piece for football as \
     there is a lot of contact in this game. The helmet should be comfortable \
     and secure around your head.",
    category_id=category.id, user_id=admin.id)
session.add(item4)
session.commit()

item5 = Item(name="Football Pads",
    description="Pads should be worn by all players around the shoulder, thigh\
     hip and knees for protection from injury.",
    category_id=category.id, user_id=admin.id)
session.add(item5)
session.commit()

#Create baseball category
baseballCategory = Category(name="Baseball")
session.add(baseballCategory)
session.commit()

#Create items for the baseball category
category = session.query(Category).filter_by(name="Baseball").one()

item1 = Item(name="Cleats",
    description="Baseball requires players to run both on grass and sand. Having\
     proper cleats to give you traction on these surfaces is the recoommended \
     shoes to wear.",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Helmet",
    description="When batting, it is important to wear a helmet as the ball is \
     hard and if contact is made with the head, it can cause injury. There are \
     helemts specifically designed for baseball and is recommended.",
    category_id=category.id, user_id=admin.id)
session.add(item2)
session.commit()

item3 = Item(name="Gloves",
    description="There are gloves worn while batting but different gloves for \
     fielders who need to catch the ball. Fielding gloves are required but \
     batting gloves are not, although they help in gripping the bat",
    category_id=category.id, user_id=admin.id)
session.add(item3)
session.commit()

item4 = Item(name="Mouth Guard",
    description="Wear a mouth guard to protect your mouth area, especially your\
     teeth as this is a physical contact sport.",
    category_id=category.id, user_id=admin.id)
session.add(item4)
session.commit()

item5 = Item(name="Baseball",
    description="The baseball is necessary to play the game. The offical ball \
     has some weight and is very hard. There are also softer balls that can be \
     used for casual gameplay",
    category_id=category.id, user_id=admin.id)
session.add(item5)
session.commit()

item6 = Item(name="Bat",
    description="The bat is also necessary to play the game. They are made of \
     wood and have some weight to them. You can also use metal ones which are \
     lighter in weight.",
    category_id=category.id, user_id=admin.id)
session.add(item6)
session.commit()

#Create badminton category
badmintonCategory = Category(name="Badminton")
session.add(badmintonCategory)
session.commit()

#Create items for the badminton category
category = session.query(Category).filter_by(name="Badminton").one()

item1 = Item(name="Birdie",
    description="There are two types - plastic and feathered. Plastic are more \
     durable but are only recommended for beginners. Feathered birdies are \
     used by professionals but are far less durable.", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Racket",
    description="Rackets can be made of plastic or wood. There are a variety \
     of rackets so it depends on the player which type they prefer.", category_id=category.id, user_id=admin.id)
session.add(item2)
session.commit()

item3 = Item(name="Net",
    description="A net is needed to play the game. There are two teams who \
     play on either side of the net.", category_id=category.id, user_id=admin.id)
session.add(item3)
session.commit()

item4 = Item(name="Badminton Shoes",
    description="Badminton shoes are designed to giv better traction during \
     gameplay. Regular shoes are not recommended since they lack grip and \
     traction.", category_id=category.id, user_id=admin.id)
session.add(item4)
session.commit()

#Create soccer category
soccerCategory = Category(name="Soccer")
session.add(soccerCategory)
session.commit()

#Create items for the soccer category
category = session.query(Category).filter_by(name="Soccer").one()

item1 = Item(name="Soccer Ball",
    description="The soccer ball is necessary to play the game. Official balls \
     are made of plastic but there are different sizes for age groups.",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Cleats",
    description="Soccer is primarily played on grass. Cleats are recommended \
     for best traction and grip on grass",
    category_id=category.id, user_id=admin.id)
session.add(item2)
session.commit()

item3 = Item(name="Socks",
    description="Wear long socks that go up to your knees for shin protection \
     as well as to guard your feet from getting blisters.",
    category_id=category.id, user_id=admin.id)
session.add(item3)
session.commit()

item4 = Item(name="Mouth Guard",
    description="Wear a mouth guard to protect your mouth area, especially your\
     teeth as this is a physical contact sport.",
    category_id=category.id, user_id=admin.id)
session.add(item4)
session.commit()

item5 = Item(name="Shorts",
    description="Wear loose-fitted pair of shorts that are comofrtable to move\
     around in",
    category_id=category.id, user_id=admin.id)
session.add(item5)
session.commit()

#Create tennis category
tennisCategory = Category(name="Tennis")
session.add(tennisCategory)
session.commit()

#Create items for the tennis category
category = session.query(Category).filter_by(name="Tennis").one()

item1 = Item(name="Racket",
    description="There are a few styles - head-light and head-heavy. Depending \
     on athleticism and skills, choose the racket that is most comfortable.",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Tennis Shoes",
    description="Shoes made for tennis are recomended. That have support for \
     the ankles and comfort for lateral movement.",
    category_id=category.id, user_id=admin.id)
session.add(item2)
session.commit()

item3 = Item(name="Tennis Balls",
    description="Tennis balls usually come in packs of 3 or 4 in a bright yellow \
     color. Test out a few brands, such as Penn or Wilson, to see what you like \
     best",
    category_id=category.id, user_id=admin.id)
session.add(item3)
session.commit()

item4 = Item(name="Visor",
    description="Tennis is played on open courts, usually outdoors. Protecting \
     yourself from the sun as well as to keep excess light in your eyes is \
     why caps are recommended.",
    category_id=category.id, user_id=admin.id)
session.add(item4)
session.commit()

item4 = Item(name="Headband",
    description="Use a headband to help keep sweat off of your face and eyes.",
    category_id=category.id, user_id=admin.id)
session.add(item4)
session.commit()

#Create hockey category
hockeyCategory = Category(name="Hockey")
session.add(hockeyCategory)
session.commit()

#Create items for the hockey category
category = session.query(Category).filter_by(name="Hockey").one()

item1 = Item(name="Skates",
    description="A comfortable pair of skates is important. Make sure to find \
     the right size and that they are properly sharpend.", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Mouth Guard",
    description="Wear a mouth guard to protect your mouth area, especially your\
     teeth as this is a physical contact sport.",
    category_id=category.id, user_id=admin.id)
session.add(item2)
session.commit()

item3 = Item(name="Pads",
    description="Shoudler, elbow and knee pads are recommended for protection \
     from injury.",
    category_id=category.id, user_id=admin.id)
session.add(item3)
session.commit()

item4 = Item(name="Helmet",
    description="A helmet designed for hockey is important. These comes with \
     cages around the face for protection,",
    category_id=category.id, user_id=admin.id)
session.add(item4)
session.commit()

item5 = Item(name="Hockey Stick",
    description="A stick should be properly fitted with the right length of \
     the player.", category_id=category.id, user_id=admin.id)
session.add(item5)
session.commit()

#Create golf category
golfCategory = Category(name="Golf")
session.add(golfCategory)
session.commit()

#Create items for the golf category
category = session.query(Category).filter_by(name="Golf").one()

item1 = Item(name="Golf Ball",
    description="One of the important necessary equipment to play golf.",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Golf Clubs",
    description="There are several types of clubs, such as irons, woods, \
     wedges and putters. These are necessary for the different types of shots \
     you come across in a golf course",
    category_id=category.id, user_id=admin.id)
session.add(item2)
session.commit()

item3 = Item(name="Golf Shoes",
    description="There are special shoes to wear for golfs. They can have \
     spikes or without, which are designed to help with traction.",
    category_id=category.id, user_id=admin.id)
session.add(item3)
session.commit()

item4 = Item(name="Golf Bag",
    description="There are a lot of golf clubs depending on the shot you need \
     to take. It is important to keep all these stored in a golf bag when \
     going on a golf course.",
    category_id=category.id, user_id=admin.id)
session.add(item4)
session.commit()

item5 = Item(name="Tees",
    description="Tees are usually made of wood or plastic and are pushed into \
     the ground to hold the ball. This is to help make an easier shot for the \
     golfer.",
    category_id=category.id, user_id=admin.id)
session.add(item5)
session.commit()

#Create volleyball category
volleyballCategory = Category(name="Volleyball")
session.add(volleyballCategory)
session.commit()

#Create items for the volleyball category
category = session.query(Category).filter_by(name="Volleyball").one()

item1 = Item(name="Volleyball",
    description="The volleyball is made of leather or synthetic leather.\
     There are also smaller balls for younger age groups.",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item2 = Item(name="Knee Pads",
    description="Knee pads should be worn to protect knees when falling,\
     sliding or diving.", category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()

item3 = Item(name="Net",
    description="The net is required to play, where two teams play on either\
     side. The height of the net is the same no matter if playing on a gym \
     floor or on sand.",
    category_id=category.id, user_id=admin.id)
session.add(item1)
session.commit()
