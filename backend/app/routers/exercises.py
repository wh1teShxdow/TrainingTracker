from fastapi import APIRouter

router = APIRouter(
    prefix="/api/exercises",
    tags=["Exercises"],

)

@router.get("/")
def get_exercises():
    return[
        {
            "id": 1,
            "name": "Bench Press",
            "muscle_group": "Chest",
        },
        {
            "id": 2,
            "name": "Squat",
            "muscle_group": "Legs",
        },
        {
            "id": 3,
            "name": "Lat Pulldown",
            "muscle_group": "Back",
        },
    ]