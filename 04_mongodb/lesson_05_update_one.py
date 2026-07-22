# Lesson 05: Update document query matching
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["BackendLearningDB"]

students = db["students"]

result = students.update_one(
    {"name": "Bharath"},
    {
        "$set": {
            "age": 22
        }
    }
)

print("Matched Documents :", result.matched_count)
print("Modified Documents:", result.modified_count)
