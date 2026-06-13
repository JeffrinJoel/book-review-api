from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    
class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True)
    bookname = Column(String)
    author = Column(String)
    genre = Column(String)
    
class Review(Base):
    __tablename__ = "reviews"
    
    id = Column(Integer, primary_key=True)
    bookname = Column(String)
    rating = Column(Integer)
    review = Column(String)