from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    username = Column(String(100), unique=True)
    password_hash = Column(String(100))
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'username' : self.username,
            'created_at' : self.created_at
        }

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow(), onupdate=datetime.datetime.utcnow())
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name' : self.name,
            'description' : self.description,
            'created_at' : self.created_at,
            'updated_at' : self.updated_at,
            'category_id' : self.category_id,
            'user_id' : self.user_id
        }

engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
