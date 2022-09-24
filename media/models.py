from sqlalchemy import Column, Integer, String, Boolean
# from database import Base
from sqlalchemy.orm import relationship

from media.database import Base


class Media(Base):
    __tablename__ = "media_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100), index=True, unique=True)
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
    streaming_source = Column(String(length=200))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(length=200))
    username = Column(String(length=200))
    password = Column(String(length=100))
    firstname = Column(String(length=100))
    lastname = Column(String(length=100))
    verified = Column(Boolean, default=False)
    active = Column(Boolean, default=False)
