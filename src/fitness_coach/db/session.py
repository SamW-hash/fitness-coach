from sqlalchemy import create_engine
from collections.abc import Generator
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

DATABASE_URL = "postgresql+psycopg://fitness:fitness@localhost:5432/fitness"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(engine, autoflush=False, expire_on_commit=True)

class Base(DeclarativeBase):
    pass

def get_db() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session