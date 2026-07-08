from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Exercise(Base):

    __tablename__ = "exercises"

    # Primary Key
    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    #Display name
    name: Mapped[str] =mapped_column(
        String(120),
        unique=True,
        nullable=False,
    )

    # Example:
    # Chest
    # Back
    # Legs
    muscle_group: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    # Longer description.
    description: Mapped[str] = mapped_column(
        String(500),
        default="",
    )