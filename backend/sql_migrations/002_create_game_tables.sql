-- Tabla para los personajes de los usuarios
CREATE TABLE IF NOT EXISTS characters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    level INTEGER NOT NULL DEFAULT 1,
    user_id UUID NOT NULL,
    profession_id INTEGER NOT NULL,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_profession
        FOREIGN KEY(profession_id)
        REFERENCES professions(id)
        ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_characters_user_id ON characters(user_id);

-- Tabla para registrar las partidas en las mazmorras
CREATE TABLE IF NOT EXISTS dungeon_runs (
    id SERIAL PRIMARY KEY,
    score INTEGER NOT NULL DEFAULT 0,
    completed_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    is_successful BOOLEAN NOT NULL DEFAULT false,
    character_id INTEGER NOT NULL,
    CONSTRAINT fk_character
        FOREIGN KEY(character_id)
        REFERENCES characters(id)
        ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_dungeon_runs_character_id ON dungeon_runs(character_id);