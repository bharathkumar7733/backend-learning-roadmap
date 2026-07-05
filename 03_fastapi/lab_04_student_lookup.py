from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    branch: str
    college: str
@app.get("/student/{student_id}")
def get_student(student_id: int):
    # In a real application, you would fetch the student details from a database
    # Here, we are returning a dummy student for demonstration purposes
    dummy_student = Student(
        name="John Doe",
        age=20,
        branch="Computer Science",
        college="XYZ University"
    )
    return {
        "student_id": student_id,
        "student": dummy_student
    }