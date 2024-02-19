from sqlalchemy import create_engine, Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from app.config.db import Base


class Thread(Base):
    __tablename__ = 'threads'

    id = Column(Integer, primary_key=True)
    identifier = Column(String(255))
