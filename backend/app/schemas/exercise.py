"""

"""

from pydantic import BaseModel


class ExerciseResponse(BaseModel):
    id: int
    
    name: str

    muscle_group: str

    description: str

    class Config:
        from_attributes = True