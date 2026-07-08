from app.database.database import engine
from app.database.base import Base
from app.models.exercise import Exercise

# Create all tables
def create_tables():
    Base.metadata.create_all(
        bind=engine
    )

if __name__ == "__main__":
    create_tables()