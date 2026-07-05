from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    book_id: int
    title: str
    author: str
    price: int

books = []

@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return {
        "message": "Book Added Successfully",
        "book_id": book.book_id,
        "book": book
    }

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.book_id == book_id:
            return {
                "message": "Book Retrieved Successfully",
                "book": book
            }
    return {"message": "Book not found"}

@app.get("/books")
def get_books():
    return {"books": books}
