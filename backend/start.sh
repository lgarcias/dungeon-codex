#!/bin/bash
set -e # Salir inmediatamente si un comando falla.

# Navegar al directorio del script para que las rutas relativas funcionen.
cd "$(dirname "$0")"

echo "📦 Applying database migrations..."
python apply_migrations.py

echo "🚀 Starting Dungeon Codex API..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
