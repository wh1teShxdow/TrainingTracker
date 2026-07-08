from datetime import datetime
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Workout(Base):

    __tablename__ = "workouts"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    notes: Mapped[str] = mapped_column(
        String(500),
        default=""
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )