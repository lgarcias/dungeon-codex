from fastapi import FastAPI
from app.api.routes import users, dungeon, characters, professions, auth

app = FastAPI()

# Register routers
app.include_router(users.router)
app.include_router(dungeon.router, prefix="/dungeon", tags=["Dungeon"])
app.include_router(characters.router, prefix="/characters", tags=["Characters"])
app.include_router(professions.router, prefix="/professions", tags=["Professions"])
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Dungeon Codex API"}
