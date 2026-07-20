from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["BackendLearningDB"]

students = db["students"]

student = students.find_one({"name": "Bharath"})

print(student)