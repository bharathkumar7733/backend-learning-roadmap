# Lab 10: Optional query parameters implementation
from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "bookname": "Python",
        "author": "Guido",
        "price": 500
    },
    {
        "id": 2,
        "bookname": "FastAPI",
        "author": "Sebastian",
        "price": 600
    },
    {
        "id": 3,
        "bookname": "Python Advanced",
        "author": "Guido",
        "price": 700
    },
    {
        "id": 4,
        "bookname": "Java",
        "author": "James",
        "price": 400
    }
]
filetered_books = []

@app.get("/books")
def get_books(author: str | None = None):
    if author is None:
        return books
    print(f"Searching books for author: {author}")
    filetered_books.clear()
    for book in books:
        if book["author"] == author:
            filetered_books.append(book)
    return filetered_books
