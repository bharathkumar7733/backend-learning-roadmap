# Lab 11: Local vs global state query parameter example
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
@app.get("/books")
def get_books(author : str | None = None):
    if author is None:
        return books
    filtered_books = []
    print(f"Searching books for author: {author}")
    for book in books:
        if book["author"] == author:
            filtered_books.append(book)
    return filtered_books
