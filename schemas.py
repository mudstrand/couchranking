from pydantic import BaseModel

class Media(BaseModel):
    title: str
    year: int
