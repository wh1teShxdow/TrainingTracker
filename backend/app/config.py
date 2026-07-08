"""
TrainingTracker Backend

File:
    config.py


"""

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Load Config values from .env
    """

    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"

settings = Settings()