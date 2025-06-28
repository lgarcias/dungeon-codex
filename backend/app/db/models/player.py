from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    level = Column(Integer, default=1)
    