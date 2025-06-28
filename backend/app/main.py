from fastapi import FastAPI
from app.api.routes import players

app = FastAPI()

app.include_router(players.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Dungeon Codex API"}
