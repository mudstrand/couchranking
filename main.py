from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from media import models
from media import models
from media.database import engine
# from media.routers import media, user
import uvicorn

from media.routers import media, user

app = FastAPI()

models.Base.metadata.create_all(engine)

origins = [
    "http://localhost:3000",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(media.router)
app.include_router(user.router)
# On the command line
# uvicorn main:app --host 0.0.0.0 --port 8000
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
