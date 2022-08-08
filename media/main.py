from fastapi import FastAPI
from media import models
from media.database import engine
from media.routers import media, user
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(media.router)
app.include_router(user.router)
# On the command line
# uvicorn main:app --host 0.0.0.0 --port 8000
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)