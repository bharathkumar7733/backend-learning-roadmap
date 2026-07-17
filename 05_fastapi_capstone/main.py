# Student Management Capstone Main Entrypoint
from fastapi import FastAPI

from routes import router


app = FastAPI(
    title="Student Management API",
    description="FastAPI capstone project for managing students",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Student Management API is running"
    }
