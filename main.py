import fastapi
import uvicorn
from api import home

api = fastapi.FastAPI()


def configure():
    api.include_router(home.router)


configure()

if __name__ == '__main__':
    uvicorn.run("main:api", reload=True)