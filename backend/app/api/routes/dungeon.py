from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.schemas.dungeon_run import DungeonRunCreate, DungeonRunRead
from app.db.models.dungeon_run import DungeonRun
from sqlalchemy.future import select

router = APIRouter()

@router.post("/dungeon/end", response_model=DungeonRunRead)
async def end_dungeon_run(dungeon_run: DungeonRunCreate, db: AsyncSession = Depends(get_db)):
    new_dungeon_run = DungeonRun(**dungeon_run.dict())
    db.add(new_dungeon_run)
    await db.commit()
    await db.refresh(new_dungeon_run)
    return new_dungeon_run
