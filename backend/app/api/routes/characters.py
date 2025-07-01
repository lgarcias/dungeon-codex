from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.schemas.character import CharacterCreate, CharacterRead
from app.db.models.character import Character
from sqlalchemy.future import select

router = APIRouter()

@router.post("/characters", response_model=CharacterRead)
async def create_character(character: CharacterCreate, db: AsyncSession = Depends(get_db)):
    new_character = Character(**character.dict())
    db.add(new_character)
    await db.commit()
    await db.refresh(new_character)
    return new_character

@router.get("/characters", response_model=list[CharacterRead])
async def get_characters(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Character))
    return result.scalars().all()

@router.get("/characters/{character_id}", response_model=CharacterRead)
async def get_character(character_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Character).where(Character.id == character_id))
    character = result.scalar()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character
