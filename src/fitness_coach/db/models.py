from .session import Base
from sqlalchemy.orm import Mapped, mapped_column

class Measurement(Base):
    __tablename__ = "measurements"
    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[str] = mapped_column(nullable=False)
    weight: Mapped[float] = mapped_column(nullable=False)
    steps: Mapped[int] = mapped_column(nullable=False)