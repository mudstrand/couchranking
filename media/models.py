from sqlalchemy import Column, Integer, String
from . database import Base
from sqlalchemy.orm import relationship


class Media(Base):
    __tablename__ = "media_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100))
    year = Column(Integer)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100))
    email = Column(String(length=100))
    password = Column(String(length=100))