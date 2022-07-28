from typing import Optional

import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/')
def index():
    return {"message": "Hello World",
            "status": "OK"}

@api.get('/items/item_id')
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


uvicorn.run(api)