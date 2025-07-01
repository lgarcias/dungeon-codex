from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DungeonRunCreate(BaseModel):
    score: Optional[int] = 0
    is_successful: Optional[bool] = False
    character_id: int

class DungeonRunRead(BaseModel):
    id: int
    score: int
    completed_at: datetime
    is_successful: bool
    character_id: int

    class Config:
        orm_mode = True
