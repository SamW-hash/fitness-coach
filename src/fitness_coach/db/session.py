from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://fitness:fitness@localhost:5432/fitness"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(engine, autoflush=False, expire_on_commit=True)

class Base(DeclarativeBase):
    pass
