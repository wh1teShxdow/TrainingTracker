from app.database.database import SessionLocal
from app.models.exercise import Exercise

def seed():

    db = SessionLocal()

    exercises = [

        Exercise(
            name="Bench Press",
            muscle_group="Chest",
            description="Barbell chest press",
        ),

        Exercise(
            name="Squat",
            muscle_group="Legs",
            description="Barbell squat",
        ),

        Exercise(
            name="Lat Pulldown",
            muscle_group="Back",
            description="Cable lat pulldown",
        ),
    ]

    db.add_all(exercises)
    db.commit() 
    db.close()

if __name__ == "__main__":
    seed()