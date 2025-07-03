from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas
from app.db.database import get_db
from app.db.models.character import Character
from app.db.models.profession import Profession
from sqlalchemy.future import select

router = APIRouter()

@router.post("", response_model=schemas.CharacterRead)
async def create_character(character: schemas.CharacterCreate, db: AsyncSession = Depends(get_db)):
    # Fetch the chosen profession to get base stats and inventory
    profession_result = await db.execute(
        select(Profession).where(Profession.id == character.profession_id)
    )
    profession = profession_result.scalar_one_or_none()

    if not profession:
        raise HTTPException(
            status_code=404,
            detail=f"Profession with id {character.profession_id} not found",
        )

    # Create the character instance using the profession's base values
    character_data = character.model_dump(exclude={"stats", "inventory"})
    new_character = Character(
        **character_data, stats=profession.base_stats, inventory=profession.base_inventory
    )

    db.add(new_character)
    await db.commit()
    await db.refresh(new_character)
    return new_character