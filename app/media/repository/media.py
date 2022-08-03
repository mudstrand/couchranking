from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    media_items = db.query(models.Media).all()
    return media_items


def create(request: schemas.Media, db: Session):
    new_media = models.Media(title=request.title, body=request.year, user_id=1)
    db.add(new_media)
    db.commit()
    db.refresh(new_media)
    return new_media


def destroy(id: int, db: Session):
    media_item = db.query(models.Media).filter(models.Media.id == id)

    if not media_item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Media item with id {id} not found")

    media_item.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Media, db: Session):
    media_item = db.query(models.Media).filter(models.Media.id == id)

    if not media_item.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Media item with id {id} not found")

    media_item.update(request.dict())
    db.commit()
    return 'updated'


def show(id: int, db: Session):
    media_item = db.query(models.Media).filter(models.Media.id == id).first()
    if not media_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Media item with the id {id} is not available")
    return media_item