"""
File: main.py
Purpose: 
    API Entry point

Author: Me



"""

#Import FastAPI.

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import exercises


app = FastAPI(
    title="Training Tracker",
    description="Backend API",
    version="0.1.0",
)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(exercises.router)

# Root endpoint for verification that backend is running
@app.get("/")
def root():
    return {
        "message": "Welcome",
        "status": "Backend running successfully",
        "version": "0.1.0",
        "developer": "Cameron Davids",
        "exercises": "",
    }