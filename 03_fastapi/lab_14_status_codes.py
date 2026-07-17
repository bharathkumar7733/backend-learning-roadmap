# Lab 14: Using explicit HTTP status codes in responses
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int


students = []


@app.post(
    "/student",
    status_code=status.HTTP_201_CREATED
)
def create_student(student: Student):

    students.append(student)

    return {
        "message": "Student created successfully",
        "student": student
    }


@app.get("/students")
def get_students():

    return students
