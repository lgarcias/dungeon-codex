from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas
from app.db.database import get_db
from app.db.models.dungeon_run import DungeonRun

router = APIRouter()

@router.post("/end", response_model=schemas.DungeonRunRead)
async def end_dungeon_run(dungeon_run: schemas.DungeonRunCreate, db: AsyncSession = Depends(get_db)):
    new_dungeon_run = DungeonRun(**dungeon_run.model_dump())
    db.add(new_dungeon_run)
    await db.commit()
    await db.refresh(new_dungeon_run)
    return new_dungeon_run