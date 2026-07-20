from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["BackendLearningDB"]

students = db["students"]

all_students = students.find()

for student in all_students:
    print(student)