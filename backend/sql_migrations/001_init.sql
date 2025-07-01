-- 001_init.sql

CREATE TABLE users (
    id UUID PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE professions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT
);

CREATE TABLE characters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    level INTEGER DEFAULT 1,
    user_id UUID NOT NULL REFERENCES users(id),
    profession_id INTEGER NOT NULL REFERENCES professions(id)
);

CREATE TABLE dungeon_runs (
    id SERIAL PRIMARY KEY,
    score INTEGER NOT NULL DEFAULT 0,
    completed_at TIMESTAMPTZ DEFAULT now(),
    is_successful BOOLEAN NOT NULL DEFAULT false,
    character_id INTEGER NOT NULL REFERENCES characters(id)
);
