from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["BackendLearningDB"]
students = db["students"]
print("Connected Successfully")