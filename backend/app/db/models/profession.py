from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.dialects.postgresql import JSONB
from app.db.base import Base

class Profession(Base):
    __tablename__ = 'professions'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    base_stats = Column(JSONB, nullable=True)
    base_inventory = Column(JSONB, nullable=True)
