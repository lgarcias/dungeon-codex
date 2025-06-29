-- 001_init.sql

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    level INTEGER DEFAULT 1
);