from pydantic import BaseModel, ConfigDict
from datetime import datetime
from decimal import Decimal
from uuid import UUID

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

class BodyMeasurementCreate(BaseModel):
    measured_at: datetime
    source_provider: str
    source_measurement_id: str | None = None
    weight_kg: Decimal | None = None
    fat_mass_kg: Decimal | None = None
    fat_free_mass_kg: Decimal | None = None
    muscle_mass_kg: Decimal | None = None
    bone_mass_kg: Decimal | None = None
    water_mass_kg: Decimal | None = None
    standing_heart_rate_bpm: int | None = None

class BodyMeasurementRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    measured_at: datetime
    source_provider: str
    source_measurement_id: str | None = None
    weight_kg: Decimal | None = None
    fat_mass_kg: Decimal | None = None
    fat_free_mass_kg: Decimal | None = None
    muscle_mass_kg: Decimal | None = None
    bone_mass_kg: Decimal | None = None
    water_mass_kg: Decimal | None = None
    standing_heart_rate_bpm: int | None = None