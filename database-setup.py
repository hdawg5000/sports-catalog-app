from sqlalchemy import Column, Integer, String, create_engine
from sqlachemy.orm import sessionmaker, relationship
from sqlachemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    password_hash = Column(String(100))

class Category(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


class Item(Base):
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
