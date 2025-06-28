### backend/app/api/routes/players.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.schemas.player import PlayerCreate, PlayerRead
from app.db.models.player import Player
from app.db.database import get_db

router = APIRouter(prefix="/players", tags=["players"])

@router.post("/", response_model=PlayerRead)
async def create_player(player: PlayerCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Player).where(Player.username == player.username))
    existing = result.scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_player = Player(username=player.username)
    db.add(new_player)
    await db.commit()
    await db.refresh(new_player)
    return new_player


@router.get("/", response_model=list[PlayerRead])
async def list_players(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Player))
    players = result.scalars().all()
    return players
