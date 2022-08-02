import fastapi
from starlette.requests import Request

from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT
from fastapi import FastAPI, Body, Depends

router = fastapi.APIRouter()

@router.get('/rank/{id}')
async def rank_by_id(request: Request):
    rank_dict = {}
    rank_dict['title'] = 'the grey man'
    rank_dict['title'] = 'the old man'
    return rank_dict

@router.get('/', dependencies=[Depends(JWTBearer())])
async def index(request: Request):
    my_dict = {}
    my_dict['message'] = 'Hello World'
    my_dict['status'] = '110'
    return my_dict
