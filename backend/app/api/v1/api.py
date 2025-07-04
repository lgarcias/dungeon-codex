from fastapi import APIRouter

from app.api.v1.endpoints import auth, professions, characters, dungeon, users

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(professions.router, prefix="/professions", tags=["professions"])
api_router.include_router(characters.router, prefix="/characters", tags=["characters"])
api_router.include_router(dungeon.router, prefix="/dungeon", tags=["dungeon"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
