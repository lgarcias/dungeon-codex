from pydantic import BaseModel

class ProfessionCreate(BaseModel):
    name: str
    description: str

class ProfessionRead(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True
