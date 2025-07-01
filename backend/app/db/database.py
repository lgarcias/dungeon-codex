from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Synchronous database URL for Alembic migrations
def get_sync_database_url():
    """
    Returns the synchronous database URL.
    Useful for tools like Alembic that might not work with async drivers.
    The print statement is kept for debugging purposes during migrations.
    """
    print(f"🔍 Full DB URL: {settings.SYNC_DATABASE_URL}")
    return settings.SYNC_DATABASE_URL
    

# Crear el engine
engine = create_async_engine(settings.ASYNC_DATABASE_URL, echo=settings.DB_ECHO)

# Crear el sessionmaker
async_session = sessionmaker(   
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# Dependency para usar en los endpoints
async def get_db():
    async with async_session() as session:
        yield session

