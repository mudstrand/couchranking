from typing import List, Optional
from pydantic import BaseModel


class User(BaseModel):
    name:str
    email:str
    password:str


class Media(BaseModel):
    title: str
    year: int


class ShowUser(BaseModel):
    name:str
    email:str
    media_items : List[Media] =[]

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str

