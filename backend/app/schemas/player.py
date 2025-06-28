### backend/app/schemas/player.py
from pydantic import BaseModel

class PlayerCreate(BaseModel):
    username: str

class PlayerRead(BaseModel):
    id: int
    username: str
    level: int

    class Config:
        orm_mode = True
