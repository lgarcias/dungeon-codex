from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_password_hash
from app.db.models.user import User
from app.schemas.user import UserCreate


async def get_user_by_email(db: AsyncSession, *, email: str) -> User | None:
    """
    Busca un usuario por su email.
    """
    result = await db.execute(select(User).filter(User.email == email))
    return result.scalars().first()


async def create_user(db: AsyncSession, *, user_in: UserCreate) -> User:
    """
    Crea un nuevo usuario en la base de datos.
    """
    hashed_password = get_password_hash(user_in.password)
    db_user = User(
        username=user_in.username,
        email=user_in.email,
        password_hash=hashed_password,
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user