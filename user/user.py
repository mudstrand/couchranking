# from fastapi import APIRouter
# import database, schemas, models
# from sqlalchemy.orm import Session
# from fastapi import APIRouter, Depends, status
# from repository import user
#
# routers = APIRouter(
#     prefix="/user",
#     tags=['Users']
# )
#
# get_db = database.get_db
#
#
# @routers.post('/', response_model=schemas.ShowUser)
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     return user.create(request, db)
#
#
# @routers.get('/{id}', response_model=schemas.ShowUser)
# def get_user(id: int, db: Session = Depends(get_db)):
#     return user.show(id, db)