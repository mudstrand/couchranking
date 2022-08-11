import json

from fastapi import Depends, APIRouter, status, Response, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import media
from ..movie_api.omdb_api import get_movie_details

router = APIRouter(
    # prefix="/media",
    tags=['Media']
)

get_db = database.get_db


# @router.get('/', response_model=List[schemas.Media])
# def all(db: Session = Depends(get_db)):
#     return media.get_all(db)


# @router.post('/media', status_code=status.HTTP_201_CREATED)
# def create(request: schemas.Media, db: Session = Depends(get_db)):
#     data = get_movie_details("xxxxx")
#     new_media = models.Media(
#         title=request.title,
#         year=data["Year"],
#         rated=data["Rated"],
#         writer=data["Writer"],
#         director=data["Director"],
#         genre=data["Genre"],
#         actors=data["Actors"],
#         plot=data["Plot"],
#         rating=data["imdbRating"],
#         votes=data["imdbVotes"],
#         box_office=data["BoxOffice"]
#         )
#     db.add(new_media)
#     db.commit()
#     db.refresh(new_media)
#     return new_media


@router.get('/media/load/{name}', status_code=status.HTTP_201_CREATED)
def load(name: str, db: Session = Depends(get_db)):
    try:
        data = get_movie_details(name)
    except FileNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Search for '{name}' yielded no results!")

    new_media = models.Media(
        title=data["Title"],
        year=data["Year"],
        rated=data["Rated"],
        released=data["Released"],
        runtime=data["Runtime"],
        writer=data["Writer"],
        director=data["Director"],
        genre=data["Genre"],
        type=data["Type"],
        actors=data["Actors"],
        plot=data["Plot"],
        rating=data["imdbRating"],
        votes=data["imdbVotes"],
        box_office=data.get("BoxOffice"),
        poster=data.get("Poster"),
        imdb_id=data.get("imdbID")
        )
    db.add(new_media)
    db.commit()
    db.refresh(new_media)
    return new_media


@router.get('/media')
def all(db: Session = Depends(get_db)):
    data = get_movie_details('the_anchorman')
    media_items = db.query(models.Media).all()
    return media_items


@router.get('/media/{id}', status_code=status.HTTP_200_OK)
def show(id:int, response: Response, db: Session = Depends(get_db)):
    media_item = db.query(models.Media).filter(models.Media.id == id).first()
    if not media_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Media item with id {id} is not available")
    return media_item


@router.delete('/media/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    db.query(models.Media).filter(models.Media.id == id).delete(synchronize_session=False)
    db.commit()
    return {'message': 'done'}


@router.put('/media/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Media, db: Session = Depends(get_db)):
    return media.update(id, request, db)
    # db.query(models.Media).filter(models.Media.id == id).update(request)
    # db.commit()
    # return {'message': 'updated successfully'}

@router.put('/media/source/{id}/{source}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, source: int, db: Session = Depends(get_db)):
    return media.update_source(id, source, db)