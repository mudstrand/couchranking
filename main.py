import fastapi
import uvicorn
from api import home, rank, media
import models
from database import engine

api = fastapi.FastAPI()


def configure():
    api.include_router(home.router)
    api.include_router(rank.router)
    api.include_router(media.router)


configure()

models.Base.metadata.create_all(engine)

if __name__ == '__main__':
    uvicorn.run("main:api", reload=True)