-- Insertar profesiones adicionales para el juego
INSERT INTO professions (name, description, base_stats, base_inventory) VALUES
('Mage', 'A powerful spellcaster who commands the arcane arts.', '{"hp": 70, "mana": 150, "damage": 18}', '{"staff": 1, "spellbook": 1}'),
('Rogue', 'A stealthy operative who strikes from the shadows.', '{"hp": 90, "mana": 50, "damage": 12}', '{"daggers": 2, "lockpicks": 1}')
ON CONFLICT (name) DO NOTHING;