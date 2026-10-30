from fastapi import FastAPI
from .schemas import MeasurementCreate

app = FastAPI(title="Fitness Coach API")
measurements = [{"id": 1, "date": "01/01/1999", "weight": "274.1", "steps": "1123"}, {"id": 2, "date": "06/04/2002", "weight": "183.6", "steps": "3567"}]

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/")
def home():
    return {"message": "Fitness Coach API"}

@app.get("/measurements")
def get_measurements():
    return measurements

@app.post("/measurements")
def create_measurement(measurement: MeasurementCreate):
    post_dict = measurement.model_dump()
    post_dict["id"] = max((item["id"] for item in measurements), default=0) + 1
    measurements.append(post_dict)
    return {"message": "item created", "data": post_dict}