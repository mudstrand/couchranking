from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class Media(Base):
    __tablename__ = "media_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100))
    year = Column(String(length=100))
    rated = Column(String(length=100))
    released = Column(String(length=100))
    runtime = Column(String(length=100))
    writer = Column(String(length=100))
    director = Column(String(length=100))
    genre = Column(String(length=100))
    type = Column(String(length=100))
    actors = Column(String(length=1000))
    plot = Column(String(length=5000))
    rating = Column(String(length=10))
    votes = Column(String(length=10))
    box_office = Column(String(length=30))
    poster = Column(String(length=1000))
    imdb_id = Column(String(length=20))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100))
    email = Column(String(length=100))
    password = Column(String(length=100))