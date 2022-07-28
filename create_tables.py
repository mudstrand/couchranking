import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

# Connect to MariaDB using SqlAlchemy
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://couchranking:123Fender51!@192.168.50.7:3307/couchranking")

Base = declarative_base()

class User(Base):
    __tablename__ = 'employees'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    firstname = sqlalchemy.Column(sqlalchemy.String(length=100))
    lastname = sqlalchemy.Column(sqlalchemy.String(length=100))
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

Base.metadata.create_all(engine)

