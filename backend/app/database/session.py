"""
Database Connection

Purpose:
    Create a SQLAlchemy engine and session factory

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

#Create one engine for the app
engine= create_engine(settings.database_url, echo=True)

# SessionLocal creates database sessions 
SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)