import os
import sys
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy import engine_from_config
from alembic import context

# --- Añade tu app al path ---
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# --- Importa Base y DB URL ---
from db.database import get_database_url
from db.models import Base  # Asegúrate que __init__.py importa Player

# Configuración base
config = context.config
fileConfig(config.config_file_name)

# Forzar la URL de conexión desde get_database_url
config.set_main_option("sqlalchemy.url", get_database_url())

# Conectar metadata para autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # Detecta cambios de tipo en columnas
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
