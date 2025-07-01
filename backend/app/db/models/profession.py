from sqlalchemy import Column, String, Integer, Text
from .base import Base

class Profession(Base):
    __tablename__ = 'professions'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(Text, nullable=True)
