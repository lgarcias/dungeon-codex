import os
import subprocess
from typing import AsyncGenerator, Generator
from dotenv import load_dotenv

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.main import app
from app.core.config import Settings, get_settings
from app.db.database import get_db

@pytest.fixture(scope="session")
def settings() -> Settings:
    """
    Carga la configuración desde .env-test y proporciona una instancia de Settings.
    Esto asegura que los tests usen una configuración aislada.
    """
    load_dotenv(dotenv_path=".env-test", override=True)
    get_settings.cache_clear()  # Forzar la recarga de la configuración con las variables de test
    return get_settings()

@pytest.fixture(scope="session")
def setup_database(settings: Settings):
    """
    Fixture para crear y eliminar la base de datos de test.
    Se ejecuta una vez por sesión de tests.
    """
    engine = create_engine(settings.SYNC_DATABASE_URL_TEST_ROOT, isolation_level="AUTOCOMMIT")
    
    with engine.connect() as conn:
        # Forzar la eliminación de la base de datos de test si existe para garantizar un estado limpio
        conn.execute(text(f'DROP DATABASE IF EXISTS "{settings.POSTGRES_DB_TEST}" WITH (FORCE)'))
        print(f"Base de datos de test '{settings.POSTGRES_DB_TEST}' eliminada (si existía).")

        # Crear una base de datos de test nueva
        conn.execute(text(f'CREATE DATABASE "{settings.POSTGRES_DB_TEST}"'))
        print(f"Base de datos de test '{settings.POSTGRES_DB_TEST}' creada.")

    # Ejecutar las migraciones
    print("Aplicando migraciones a la base de datos de test...")
    # Usamos el script que ya tienes para mantener la consistencia
    subprocess.run(
        ["python", "apply_migrations.py"],
        check=True,
        cwd="backend", # Ejecutar desde el directorio del backend
        env={**os.environ, "POSTGRES_DB": settings.POSTGRES_DB_TEST} # Sobrescribimos la DB a usar
    )
    print("Migraciones aplicadas.")

    yield

    # with engine.connect() as conn:
    #     conn.execute(text(f'DROP DATABASE "{settings.POSTGRES_DB_TEST}" WITH (FORCE)'))
    #     print(f"Base de datos '{settings.POSTGRES_DB_TEST}' eliminada.")


@pytest_asyncio.fixture(scope="function")
async def db_session(settings: Settings, setup_database: None) -> AsyncGenerator[AsyncSession, None]:
    """
    Proporciona una sesión de base de datos de test para cada test.
    """
    engine = create_async_engine(settings.ASYNC_DATABASE_URL_TEST)
    AsyncSessionLocal = async_sessionmaker(
        autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
    )
    async with AsyncSessionLocal() as session:
        yield session


@pytest_asyncio.fixture(scope="function")
async def client(db_session: AsyncSession) -> AsyncGenerator[AsyncClient, None]:
    """
    Proporciona un cliente HTTP asíncrono para realizar peticiones a la API.
    """
    
    # Sobrescribir la dependencia get_db para que use la sesión de test
    def get_test_db_session() -> Generator[AsyncSession, None, None]:
        yield db_session

    app.dependency_overrides[get_db] = get_test_db_session

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as async_client:
        yield async_client
    
    # Limpiar la sobrescritura después del test
    app.dependency_overrides.clear()