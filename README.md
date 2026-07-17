# 🚀 FastAPI Backend Learning Journey

This repository documents my complete backend learning journey from scratch using FastAPI.

The goal is to build strong backend fundamentals before moving to MongoDB, JWT Authentication, AI APIs, RAG, LLMs, System Design, and Enterprise AI projects.

---

# 📚 Learning Roadmap

```
Python
        ↓
REST API
        ↓
FastAPI
        ↓
CRUD APIs
        ↓
Project Structure
        ↓
MongoDB
        ↓
JWT Authentication
        ↓
AI Integration
        ↓
RAG
        ↓
LLMs
        ↓
Enterprise AI Projects
```

---

# 📂 Repository Structure

```
backend-learning-roadmap/

├── 01_python_basics/
├── 02_rest_api/
├── 03_fastapi/
├── 04_project_structure/
├── 05_fastapi_capstone/
└── README.md
```

---

# 📚 FastAPI Lessons Completed

## ✅ Lesson 01 – First FastAPI Application

### Concepts
- FastAPI Installation
- Uvicorn
- First GET API
- Returning JSON

---

## ✅ Lesson 02 – Multiple Routes

### Concepts

- API Routing
- Multiple Endpoints
- JSON Responses

Routes

- GET /
- GET /student
- GET /teacher
- GET /skills
- GET /college

---

## ✅ Lesson 03 – POST Requests

### Concepts

- POST Request
- BaseModel
- Request Body
- JSON Validation
- Python Object
- JSON Conversion

Mini Project

- Student Registration API

---

## ✅ Lesson 09 – CRUD API Fundamentals

### Concepts

- REST API Design
- CRUD Operations
- Temporary Database
- Path Parameters
- Request Body

---

# 🧪 Lab 05 – Mini Library API

### Features

- Add Book
- View One Book
- View All Books

### APIs

POST /book

GET /books

GET /books/{book_id}

---

# 🧪 Lab 06 – Automatic Book ID Generation

### Features

- Backend Generated IDs
- Store Books
- Retrieve Books

### Concepts

- append()
- Python Dictionary
- Temporary Database
- CRUD Foundation

---

# 🧪 Lab 07 – Update Book API

### Features

- Update Existing Book

### API

PUT /books/{book_id}

### Concepts

- PUT Request
- Dictionary Update
- Searching by ID

---

# 🧪 Lab 08 – Delete Book API

### Features

- Delete Existing Book

### API

DELETE /books/{book_id}

### Concepts

- DELETE Request
- remove()
- Complete CRUD

---

# 🧪 Lab 09 – Query Parameters

## Objective

Learn how to filter resources using Query Parameters.

### API

GET /books?author=Guido

### Features

- Search books by author
- Return multiple matching records
- Learn filtering concepts

### Concepts Learned

- Query Parameters
- Filtering Data
- FastAPI Query Variables
- Searching Lists
- append()

---

# 🧪 Lab 10 – Optional Query Parameters

### Features
- Search books by author optionally
- Return all books if no author parameter is provided

### Concepts Learned
- Optional Query Parameters (`author: str | None = None`)
- Type hinting with Union/Optional types

---

# 🧪 Lab 11 – Local vs Global Filtering State

### Features
- Thread-safe and request-isolated filtering state

### Concepts Learned
- Defining temporary lists locally inside functions rather than globally
- Avoiding state persistence bugs in FastAPI backends

---

# 🧪 Lab 12 – Multiple Query Parameters

### Features
- Filter books on multiple fields (author and price) simultaneously

### Concepts Learned
- Combining multiple query parameters
- Multi-conditional matching logic

---

# 🧪 Lab 13 – Response Models

### Features
- Secure student registration API by hiding sensitive data

### Concepts Learned
- `response_model` parameter in path decorators
- Filtering database fields dynamically on output using Pydantic models (e.g. hiding password fields)

---

# 🧪 Lab 14 – HTTP Status Codes

### Features
- Setting standard HTTP status codes on API responses (e.g. `201 Created` on resource creation)

### Concepts Learned
- Using `status_code` in path decorators
- Using `status` from `fastapi` module

---

# 🧪 Lab 15 – Validation & Exception Handling

### Features
- Validating Pydantic fields (e.g., minimum name length and minimum age limit)
- Raising HTTP exceptions for missing resources (e.g., return `404 Not Found` for invalid student IDs)

### Concepts Learned
- Using Pydantic's `Field` for input validation (e.g., `min_length=2`, `gt=17`)
- Raising `HTTPException` dynamically in path operations

---

# 🎓 FastAPI Capstone – Student Management API

### Features
- Create Student with age, branch, email validation
- Retrieve Single Student by ID or All Students
- Update and Delete Student operations
- Modular project layout separation (`main.py`, `models.py`, `routes.py`, `database.py`)

### Concepts Learned
- Combining all FastAPI CRUD concepts into a production-like structure
- Pydantic EmailStr validation
- APIRouter structuring

---

# 🧪 Lesson 10 – Professional Project Structure

## Folder Structure

```
04_project_structure/

├── main.py
├── models.py
├── routes.py
└── database.py
```

---

## Concepts Learned

### main.py

- Starts FastAPI Application
- Includes Routers
- Entry Point of Project

---

### models.py

Contains all Pydantic Models.

Example

- Book
- Student
- Employee
- Complaint

---

### routes.py

Contains all API Endpoints.

Example

- POST
- GET
- PUT
- DELETE

---

### database.py

Contains application data.

Currently

```python
books = []
```

Future

- MongoDB
- PostgreSQL

---

## New FastAPI Concepts

- APIRouter()
- include_router()
- Project Separation
- Code Reusability
- Modular Backend Design

---

# 📖 Mini Library Backend Features

| HTTP Method | Endpoint | Purpose |
|--------------|----------|---------|
| POST | /book | Create Book |
| GET | /books | Get All Books |
| GET | /books/{book_id} | Get One Book |
| PUT | /books/{book_id} | Update Book |
| DELETE | /books/{book_id} | Delete Book |

---

# 🧠 Python Concepts Practiced

- Variables
- Lists
- Dictionaries
- Functions
- Classes
- Objects
- Loops
- Conditions
- append()
- remove()

---

# 🚀 FastAPI Concepts Practiced

- FastAPI
- Routing
- APIRouter
- GET
- POST
- PUT
- DELETE
- BaseModel
- Path Parameters
- Query Parameters
- Response Models
- HTTP Status Codes
- Exception Handling
- JSON Request Body
- JSON Response
- Modular Project Structure

---

# 🎯 Next Learning Goals

- MongoDB Integration
- JWT Authentication
- AI APIs
- RAG
- LLM Applications
- Enterprise Backend Development


