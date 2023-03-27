from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import os

DATABASE_URL = "sqlite:///./app.db"  # Use a different DB (e.g., PostgreSQL) in production

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def get_db():
    with session_scope() as session:
        yield session