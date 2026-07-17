# Student Management Capstone API Routes
from fastapi import APIRouter, HTTPException, status

from database import students
import database

from models import StudentCreate, StudentResponse


router = APIRouter()


@router.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(student: StudentCreate):
    student_id = database.next_student_id
    database.next_student_id += 1

    new_student = {
        "id": student_id,
        "name": student.name,
        "age": student.age,
        "branch": student.branch,
        "email": student.email,
        "password": student.password
    }

    students.append(new_student)

    return new_student

@router.get(
    "/students",
    response_model=list[StudentResponse]
)
def get_all_students():

    return students
@router.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(student_id: int):

    for student in students:

        if student["id"] == student_id:
            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )

@router.put(
    "/students/{student_id}",
    response_model=StudentResponse
)
def update_student(student_id: int, updated_student: StudentCreate):

    for student in students:

        if student["id"] == student_id:
            student["name"] = updated_student.name
            student["age"] = updated_student.age
            student["branch"] = updated_student.branch
            student["email"] = updated_student.email
            student["password"] = updated_student.password

            return student

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )


@router.delete(
    "/students/{student_id}",
    status_code=status.HTTP_200_OK
)
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:
            students.remove(student)

            return {
                "message": "Student deleted successfully",
                "student_id": student_id
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Student not found"
    )
