from .player import Player
from sqlalchemy.orm import declarative_base

Base = Player.__bases__[0]  # Usamos la misma Base de player
