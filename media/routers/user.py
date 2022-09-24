from media import database, schemas
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from media.repository import user
from starlette.requests import Request

from media.auth.auth_handler import sign_jwt
from media.auth.auth_bearer import JWTBearer

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db

@router.post('/login', response_model=schemas.UserLoginResponse)
async def user_login(request: schemas.UserLogin):
    email = request.email
    password = request.password
    token = sign_jwt(email)
    roles = get_roles(email)
    rv = schemas.UserLoginResponse(access_token = token, roles = roles)
    return(rv)


def get_roles(email):
    return ['admin', 'ranked']

# this is a method to just test security
@router.get('/rank', dependencies=[Depends(JWTBearer())])
def get_rank(request: Request, db: Session = Depends(get_db)):
    my_dict = {}
    my_dict['message'] = 'Hello World'
    my_dict['status'] = '110'
    return my_dict

@router.post('/register', response_model=schemas.User)
def create_user(request: schemas.UserRegister, db: Session = Depends(get_db)):
    print("got here")
    return user.create(request, db)



@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)