from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["BackendLearningDB"]
students = db["students"]

new_student = {
    "name": "John Doe",
    "age": 20,
    "branch": "Computer Science"

}   

result = students.insert_one(new_student)
print("Inserted student with ID:", result.inserted_id)

