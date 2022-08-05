from media import database, schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from media.repository import user
from starlette.requests import Request

from media.auth.auth_handler import signJWT
from media.auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db

@router.get('/user/login')
async def user_login(request: Request):
    return(signJWT('mark@udstrand.com'))


# this is a method to just test security
@router.get('/rank', dependencies=[Depends(JWTBearer())])
def get_rank(request: Request, db: Session = Depends(get_db)):
    my_dict = {}
    my_dict['message'] = 'Hello World'
    my_dict['status'] = '110'
    return my_dict

@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)