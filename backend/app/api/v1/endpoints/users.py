from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.db.database import get_db
from app.schemas import User, UserCreate

router = APIRouter()


@router.post(
    "/",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new user",
    description="Creates a new user with a username, email, and password.",
)
async def create_new_user(
    *, db: AsyncSession = Depends(get_db), user_in: UserCreate
) -> User:
    user = await crud.get_user_by_email(db, email=user_in.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Ya existe un usuario con este email.",
        )
    user = await crud.create_user(db=db, user_in=user_in)
    return user