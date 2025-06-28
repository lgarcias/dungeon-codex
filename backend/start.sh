#!/bin/bash
echo "📦 Applying database migrations..."
cd backend
alembic upgrade head

echo "🚀 Starting Dungeon Codex API..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
