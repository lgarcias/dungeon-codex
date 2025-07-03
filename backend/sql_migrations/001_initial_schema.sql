-- Habilitar la extensión para UUID si no está habilitada
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);

CREATE TABLE IF NOT EXISTS professions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    description TEXT,
    base_stats JSONB,
    base_inventory JSONB
);

-- Insertar algunas profesiones iniciales para que la API tenga datos
INSERT INTO professions (name, description, base_stats, base_inventory) VALUES
('Alchemist', 'A master of potions and transmutations.', '{"hp": 80, "mana": 120, "damage": 5}', '{"potions": 3, "herbs": 5}'),
('Warrior', 'A brave fighter skilled with melee weapons.', '{"hp": 120, "mana": 30, "damage": 15}', '{"sword": 1, "shield": 1}')
ON CONFLICT (name) DO NOTHING;