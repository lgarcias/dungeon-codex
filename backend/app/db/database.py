import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL

def get_database_url():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")
    return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}"

# Synchronous database URL for Alembic migrations
def get_sync_database_url():
    from dotenv import load_dotenv
    load_dotenv()

    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")

    print(f"🔍 Full DB URL: postgresql://{user}:{password}@{host}:{port}/{db}")
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"
    

# Crear el engine
engine = create_async_engine(get_database_url(), echo=True)

# Crear el sessionmaker
async_session = sessionmaker(   
    bind=engine,    # type: ignore
    class_=AsyncSession,
    expire_on_commit=False,
)

# Dependency para usar en los endpoints
async def get_db():
    async with async_session() as session: # type: ignore
        yield session
# Nota: No es necesario crear tablas aquí, ya que las migraciones se manejan con Alembic.
