from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    branch: str
    college: str


@app.post("/student")
def register_student(student: Student):
    return {
        "message": "Student Registered Successfully",
        "student": student
    }