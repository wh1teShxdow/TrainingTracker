from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    workout_id: Mapped[int] = mapped_column(
        ForeignKey("workouts.id"),
        nullable=False
    )

    exercise_id: Mapped[int] = mapped_column(
        ForeignKey("exercises.id"),
        nullable=False
    )

    sets: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    reps: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    weight: Mapped[float] = mapped_column(
        nullable=False
    )
