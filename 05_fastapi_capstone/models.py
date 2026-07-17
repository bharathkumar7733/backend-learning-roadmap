from pydantic import BaseModel, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    age: int = Field(ge=17, le=100)
    branch: str = Field(min_length=2, max_length=30)
    email: EmailStr
    password: str = Field(min_length=8)


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    branch: str
    email: EmailStr