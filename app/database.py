import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load .env to get the DATABASE_URL
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# The Engine is the starting point for SQLAlchemy
# It handles the physical connection to PostgreSQL
engine = create_engine(DATABASE_URL)

# A Session is like a local copy of the database where we can "queue" changes
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class that our models will inherit from
Base = declarative_base()

# Utility to get a database session during a request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
