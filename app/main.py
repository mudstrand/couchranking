from fastapi import FastAPI
from media import models
from media.database import engine
from media.routers import media, user
import uvicorn
# import uvicorn
# import uvicorn
# # from api import home, rank
# from app.media.routers import media, user
# from app.media import models
# from app.media.database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(media.router)
app.include_router(user.router)


# def configure():
#     api.include_router(user.router)
#     api.include_router(media.router)
#
#
# configure()
#
# models.Base.metadata.create_all(engine)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)