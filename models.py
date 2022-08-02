from sqlalchemy import Column, Integer, String
from database import Base

class Media(Base):
    __tablename__ = "media_items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100))
    year = Column(Integer)