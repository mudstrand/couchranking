from sqlalchemy.orm import Session

# from hashing import Hash
from media import models, schemas
from fastapi import HTTPException, status

from media.hashing import Hash


def create(request: schemas.UserRegister, db: Session):
    new_user = models.User(email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    rv = schemas.User(email=new_user.email)
    # db.refresh(new_user)
    return rv


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user
