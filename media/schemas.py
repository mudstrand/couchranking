from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    name:str
    email:str
    password:str


class Media(BaseModel):
    title: str
    year: str
    rated = str
    released = str
    runtime = str
    writer = str
    director = str
    genre = str
    type = str
    actors = str
    plot = str
    rating = str
    votes = str
    box_office = str
    poster = str
    imdb_id = str
    streaming_source = str

class ShowUser(BaseModel):
    name:str
    email:str
    media_items : List[Media] =[]

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str

