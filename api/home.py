import fastapi
from starlette.requests import Request

from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT
from fastapi import Depends

router = fastapi.APIRouter()

@router.get('/user/login')
async def user_login(request: Request):
    return(signJWT('mark@udstrand.com'))

@router.get('/', dependencies=[Depends(JWTBearer())])
async def index(request: Request):
    my_dict = {}
    my_dict['message'] = 'Hello World'
    my_dict['status'] = '110'
    return my_dict
