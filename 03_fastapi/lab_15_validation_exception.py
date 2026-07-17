# Lab 15: Input validation and HTTPException handling
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class Student(BaseModel):
    name: str = Field(min_length=2)
    age: int = Field(gt=17)


students = []


@app.post("/student")
def create_student(student: Student):
    students.append(student)
    return student


@app.get("/student/{student_id}")
def get_student(student_id: int):

    if student_id < 1 or student_id > len(students):
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return students[student_id - 1]
