from pydantic import BaseModel

class MeasurementCreate(BaseModel):
    date: str
    weight: float
    steps: int
