from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get('/media')
def index(limit=10, sort: Optional[str] = None):
    # only get 10 media items
    return {'data': f'{limit} media items from the db'}



@app.get('/media/{id}')
def show(id: int):
    # fetch media item with id = id
    return {'data': id}


@app.get('/media/{id}/comments')
def comments(id, limit=10):
    # fetch comments of media with id = id
    return {'data': {'1', '2'}}

class Media(BaseModel):
    title: str
    year: int

@app.post('/media')
def create_media_item(media: Media):
    return {'data': f"Media item is created with title as {media.title}"}