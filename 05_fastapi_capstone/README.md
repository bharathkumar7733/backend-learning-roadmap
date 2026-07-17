# 🎓 Student Management API (FastAPI Capstone)

A complete **Student Management REST API** built using **FastAPI** as the final capstone project of my FastAPI learning journey.

This project combines all the important FastAPI concepts learned during my backend roadmap, including CRUD operations, request validation, response models, HTTP status codes, exception handling, project structure, and routing.

---

# 🚀 Features

* Create Student
* View All Students
* View Student by ID
* Update Student
* Delete Student
* Request Validation
* Response Models
* HTTP Status Codes
* Exception Handling
* APIRouter
* Professional Project Structure

---

# 🛠️ Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

---

# 📂 Project Structure

```text
05_fastapi_capstone/
│
├── main.py
├── routes.py
├── models.py
├── database.py
├── requirements.txt
├── .env
└── README.md
```

---

# 📚 API Endpoints

## Create Student

```http
POST /students
```

Creates a new student.

### Request Body

```json
{
    "name": "Bharath",
    "age": 21,
    "branch": "IT",
    "email": "bharath@example.com",
    "password": "password123"
}
```

### Response

```json
{
    "id": 1,
    "name": "Bharath",
    "age": 21,
    "branch": "IT",
    "email": "bharath@example.com"
}
```

Status Code

```
201 Created
```

---

## Get All Students

```http
GET /students
```

Returns all students.

---

## Get Student by ID

```http
GET /students/{student_id}
```

Returns a single student using the student ID.

If the student does not exist:

```
404 Not Found
```

---

## Update Student

```http
PUT /students/{student_id}
```

Updates an existing student's information.

---

## Delete Student

```http
DELETE /students/{student_id}
```

Deletes a student from the system.

---

# 🧠 Concepts Practiced

## REST APIs

* GET
* POST
* PUT
* DELETE

---

## FastAPI

* Routing
* APIRouter
* Path Parameters
* Request Body
* JSON Responses

---

## Pydantic

* BaseModel
* Field Validation
* Email Validation
* Request Models
* Response Models

---

## Validation

Implemented validation using Pydantic.

Examples:

* Minimum name length
* Valid email format
* Age restrictions
* Password length validation

---

## HTTP Status Codes

Used appropriate status codes including:

* 200 OK
* 201 Created
* 404 Not Found

---

## Exception Handling

Implemented professional error handling using:

```python
raise HTTPException(
    status_code=404,
    detail="Student not found"
)
```

---

## Project Structure

Separated responsibilities into multiple files.

* **main.py** – Starts the FastAPI application and includes routers.
* **routes.py** – Contains all API endpoints.
* **models.py** – Defines request and response models.
* **database.py** – Stores the temporary in-memory database.

---

# ▶️ Running the Project

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start the Server

```bash
uvicorn main:app --reload
```

---

## Swagger Documentation

Open:

```
http://127.0.0.1:8000/docs
```

Swagger UI allows testing every endpoint directly from the browser.

---

# 📖 What I Learned

During this project I learned how to:

* Design REST APIs
* Build CRUD operations
* Validate incoming requests
* Hide sensitive data using Response Models
* Use proper HTTP Status Codes
* Handle errors using HTTPException
* Organize FastAPI applications into multiple files
* Build backend APIs following professional development practices

---

# 🚀 Future Improvements

This project currently uses an in-memory Python list as the database.

Future upgrades include:

* MongoDB Integration
* JWT Authentication
* Password Hashing
* Role-Based Access Control
* Pagination
* Search and Filtering
* Docker Deployment
* Cloud Deployment

---

# 🎯 Learning Roadmap

This project marks the completion of the FastAPI phase in my Backend Learning Roadmap.

```
Python Fundamentals ✅

↓

REST APIs ✅

↓

FastAPI ✅

↓

MongoDB ⏳

↓

JWT Authentication ⏳

↓

Production Backend ⏳

↓

OpenAI APIs ⏳

↓

RAG Applications ⏳

↓

Enterprise AI Projects ⏳
```

---

## 👨‍💻 Author

**Chappa Bharath Kumar**

Backend Developer | FastAPI Learner | ServiceNow Developer | AI Backend Enthusiast

This project was built as part of my journey toward becoming an AI Backend Engineer.
