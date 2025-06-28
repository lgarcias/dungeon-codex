.PHONY: dev migrate revision reset-db test

# Ejecutar el backend (desde dentro del contenedor)
dev:
	bash backend/start.sh

# Crear una nueva migración automática
revision:
	cd backend && alembic revision --autogenerate -m "auto"

# Aplicar migraciones
migrate:
	cd backend && alembic upgrade head

# Eliminar y recrear la base de datos
reset-db:
	dropdb -h $$POSTGRES_HOST -U $$POSTGRES_USER $$POSTGRES_DB || true
	createdb -h $$POSTGRES_HOST -U $$POSTGRES_USER $$POSTGRES_DB
	make migrate

# Ejecutar tests
test:
	pytest -v backend/tests
