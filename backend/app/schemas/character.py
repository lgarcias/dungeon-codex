from pydantic import BaseModel
from typing import Optional

class CharacterCreate(BaseModel):
    name: str
    level: Optional[int] = 1
    user_id: str
    profession_id: int

class CharacterRead(BaseModel):
    id: int
    name: str
    level: int
    user_id: str
    profession_id: int

    class Config:
        orm_mode = True
