import sqlalchemy
from sqlalchemy import text
# from sqlalchemy.ext.declarative import declarative_base

# Connect to MariaDB using SqlAlchemy
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://couchranking:123Fender51!@192.168.50.7:3307/couchranking")

sql = text('DROP TABLE IF EXISTS users;')
result = engine.execute(sql)
