import sqlalchemy
from sqlalchemy import text
# from sqlalchemy.ext.declarative import declarative_base

# Connect to MariaDB using SqlAlchemy
# engine = sqlalchemy.create_engine("mariadb+mariadbconnector://couchranking:123Fender51!@192.168.50.7:3307/couchranking")
engine = sqlalchemy.create_engine('postgresql://couch:couch@192.168.50.3:5432/couch')

sql = text('DROP TABLE IF EXISTS media_items;')
result = engine.execute(sql)
