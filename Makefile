.PHONY: dev migrate reset-db test install

# Instalar/actualizar dependencias
install:
	pip install -r backend/requirements.txt

# Ejecutar el backend (desde dentro del contenedor)
dev:
	bash backend/start.sh

# Aplicar migraciones de la base de datos
migrate:
	cd backend && python apply_migrations.py

# Eliminar y recrear la base de datos
reset-db:
	PGPASSWORD=$$POSTGRES_PASSWORD dropdb -h $$POSTGRES_HOST -U $$POSTGRES_USER $$POSTGRES_DB --if-exists
	PGPASSWORD=$$POSTGRES_PASSWORD createdb -h $$POSTGRES_HOST -U $$POSTGRES_USER $$POSTGRES_DB
	make migrate

# Ejecutar tests
test:
	pytest -v backend/tests
