from starlette.requests import Request

from auth.auth_bearer import JWTBearer
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get('/rank/{id}')
def rank_by_id(request: Request, db: Session = Depends(get_db)):
    rank_dict = {}
    rank_dict['title'] = 'the grey man'
    rank_dict['title'] = 'the old man'
    return rank_dict


@router.get('/', dependencies=[Depends(JWTBearer())])
def get_rank(request: Request, db: Session = Depends(get_db)):
    my_dict = {}
    my_dict['message'] = 'Hello World'
    my_dict['status'] = '110'
    return my_dict
