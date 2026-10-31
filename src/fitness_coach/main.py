from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from .schemas import MeasurementCreate
from .db.models import Measurement
from .db.session import get_db

app = FastAPI(title="Fitness Coach API")
measurements = [{"id": 1, "date": "01/01/1999", "weight": "274.1", "steps": "1123"}, {"id": 2, "date": "06/04/2002", "weight": "183.6", "steps": "3567"}]

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/")
def home():
    return {"message": "Fitness Coach API"}

@app.get("/measurements")
def get_measurements(db: Session = Depends(get_db)):
    statement = select(Measurement)
    result = db.execute(statement)
    return result.scalars().all()

@app.post("/measurements")
def create_measurement(measurement: MeasurementCreate):
    post_dict = measurement.model_dump()
    post_dict["id"] = max((item["id"] for item in measurements), default=0) + 1
    measurements.append(post_dict)
    return {"message": "item created", "data": post_dict}