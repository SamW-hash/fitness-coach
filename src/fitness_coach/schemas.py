from pydantic import BaseModel, ConfigDict

class MeasurementCreate(BaseModel):
    date: str
    weight: float
    steps: int

class MeasurementRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    date: str
    weight: float
    steps: int
