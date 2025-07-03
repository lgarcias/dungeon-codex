from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas
from app.db.database import get_db
from app.db.models.profession import Profession
from sqlalchemy.future import select

router = APIRouter()

@router.get("", response_model=list[schemas.ProfessionRead])
async def get_professions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Profession))
    return result.scalars().all()