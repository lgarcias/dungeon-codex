from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base

class DungeonRun(Base):
    __tablename__ = 'dungeon_runs'

    id = Column(Integer, primary_key=True)
    score = Column(Integer, default=0, nullable=False)
    completed_at = Column(DateTime(timezone=True), server_default=func.now())
    is_successful = Column(Boolean, default=False, nullable=False)

    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    character = relationship("Character")
