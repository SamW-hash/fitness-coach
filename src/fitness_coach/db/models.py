from uuid import UUID, uuid4
from datetime import datetime
from decimal import Decimal
from .session import Base
from sqlalchemy import DateTime, Integer, Numeric, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column

class Measurement(Base):
    __tablename__ = "measurements"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[str] = mapped_column(nullable=False)
    weight: Mapped[float] = mapped_column(nullable=False)
    steps: Mapped[int] = mapped_column(nullable=False)

class BodyMeasurement(Base):
    __tablename__ = "body_measurements"
    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    measured_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    source_provider: Mapped[str] = mapped_column(String(50), nullable=False)
    source_measurement_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    weight_kg: Mapped[Decimal | None] = mapped_column(Numeric(6, 2), nullable=True)
    fat_mass_kg: Mapped[Decimal | None] = mapped_column(Numeric(6, 2), nullable=True)
    fat_free_mass_kg: Mapped[Decimal | None] = mapped_column(Numeric(6, 2), nullable=True)
    muscle_mass_kg: Mapped[Decimal | None] = mapped_column(Numeric(6, 2), nullable=True)
    bone_mass_kg: Mapped[Decimal | None] = mapped_column(Numeric(6, 2), nullable=True)
    water_mass_kg: Mapped[Decimal | None] = mapped_column(Numeric(6, 2),nullable=True)
    standing_heart_rate_bpm: Mapped[int | None] = mapped_column(Integer, nullable=True)