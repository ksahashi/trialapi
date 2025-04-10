from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker

from env import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

DATABASE = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8"

engine = create_engine(
    DATABASE,
    echo=False,
    pool_size=10,
    max_overflow=20,
)

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
