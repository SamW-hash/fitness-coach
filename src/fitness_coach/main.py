from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from .schemas import MeasurementCreate, MeasurementRead
from .db.models import Measurement
from .db.session import get_db

app = FastAPI(title="Fitness Coach API")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/")
def home():
    return {"message": "Fitness Coach API"}

@app.get("/measurements", response_model=list[MeasurementRead])
def get_measurements(db: Session = Depends(get_db)):
    statement = select(Measurement)
    result = db.execute(statement)
    return result.scalars().all()

@app.post("/measurements", response_model=MeasurementRead)
def create_measurement(measurement: MeasurementCreate, db: Session = Depends(get_db)):
    record = Measurement(**measurement.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record