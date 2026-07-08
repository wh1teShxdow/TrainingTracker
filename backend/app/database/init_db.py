from app.database.database import engine
from app.database.base import Base
from app.models.exercise import Exercise
from app.models.workout import Workout
from app.models.workout_exercise import WorkoutExercise


# Create all tables
def create_tables():
    Base.metadata.create_all(
        bind=engine
    )

if __name__ == "__main__":
    create_tables()