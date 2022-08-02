import models
import schemas
from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT
from fastapi import FastAPI, Body, Depends, APIRouter, status, Response, HTTPException
from starlette.requests import Request
from sqlalchemy.orm import Session
from database import engine, SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/rank/{id}')
async def rank_by_id(request: Request):
    rank_dict = {}
    rank_dict['title'] = 'the grey man'
    rank_dict['title'] = 'the old man'


@router.post('/media', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Media, db: Session = Depends(get_db)):
    new_media = models.Media(title=request.title, year=request.year)
    db.add(new_media)
    db.commit()
    db.refresh(new_media)
    return new_media


@router.get('/media')
def all(db: Session = Depends(get_db)):
    media_items = db.query(models.Media).all()
    return media_items


@router.get('/media/{id}', status_code=status.HTTP_200_OK)
def show(id, response: Response, db: Session = Depends(get_db)):
    media_item = db.query(models.Media).filter(models.Media.id == id).first()
    if not media_item:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,  detail=f"Media item with id {id} is not available")
    return media_item
