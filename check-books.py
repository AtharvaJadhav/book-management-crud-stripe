from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["bookstore"]
collection = db["books"]

for book in collection.find():
    print(book)
