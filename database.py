import contextlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# db_url = "postgresql://postgres:password@localhost:5432/db_name"
DATABAE_URL = "postgresql://postgres:wldnjs5768@localhost/test_db"

engine = create_engine(DATABAE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

@contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# https://wikidocs.net/176223