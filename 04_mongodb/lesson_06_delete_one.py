# Lesson 06: Delete document query matching
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["BackendLearningDB"]

students = db["students"]

result = students.delete_one(
    {"name": "John Doe"}
)

print("Deleted Documents:", result.deleted_count)
