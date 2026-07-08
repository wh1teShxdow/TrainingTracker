from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.exercise import Exercise
from app.schemas.exercise import ExerciseResponse

router = APIRouter(
    prefix="/api/exercises",
    tags=["Exercises"],

)

@router.get("/", 
            response_model=list[ExerciseResponse])
def get_exercises(
    db: Session = Depends(get_db)
):
    exercises = db.query(
        Exercise
    ).all()
    return exercises