from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from .schemas import BodyMeasurementCreate, BodyMeasurementRead
from .db.models import BodyMeasurement
from .db.session import get_db

app = FastAPI(title="Fitness Coach API")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/")
def home():
    return {"message": "Fitness Coach API"}

@app.get("/body-measurements", response_model=list[BodyMeasurementRead])
def get_measurements(db: Session = Depends(get_db)):
    statement = select(BodyMeasurement)
    result = db.execute(statement)
    return result.scalars().all()

@app.post("/body-measurements", response_model=BodyMeasurementRead)
def create_measurement(measurement: BodyMeasurementCreate, db: Session = Depends(get_db)):
    record = BodyMeasurement(**measurement.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record