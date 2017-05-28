from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlachemy.orm import sessionmaker, relationship
from sqlachemy.ext.declarative import declarative_base

Base = declarative_base()

class Category(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

class Item(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    password_hash = Column(String(100))


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
