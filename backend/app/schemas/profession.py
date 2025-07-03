from pydantic import BaseModel
from typing import Any

class ProfessionCreate(BaseModel):
    name: str
    description: str

class ProfessionRead(BaseModel):
    id: int
    name: str
    description: str
    base_stats: dict[str, Any]
    base_inventory: dict[str, Any]

    class Config:
        orm_mode = True
