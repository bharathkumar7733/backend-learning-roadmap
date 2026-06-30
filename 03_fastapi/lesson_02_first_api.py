from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Home"}

@app.get("/student")
def student():
    return {"name": "Bharath"}

@app.get("/teacher")
def teacher():
    return {"name": "Professor"}
@app.get("/skills")
def skils():
    return {"skills": ["Python", "FastAPI", "SQLAlchemy"]}
@app.get("/college")
def college():
    return {"college": "aditya"}