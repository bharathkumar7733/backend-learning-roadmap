from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    bookname: str
    author: str
    price: int

books = []

@app.post("/book")
def create_book(book: Book):
    book_id = len(books) + 1
    new_book = {
        "id": book_id,
        "bookname": book.bookname,
        "author": book.author,
        "price": book.price
    }
    books.append(new_book)
    return {
        "message": "Book created successfully",
        "book_id": book_id,
        "book": new_book
    }

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return {
                "message": "Book Retrieved Successfully",
                "book": book
            }
    return {"message": "Book not found"}

@app.get("/books")
def get_books():
    return {"books": books}

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for book in books:
        if book["id"] == book_id:
            book["bookname"] = updated_book.bookname
            book["author"] = updated_book.author
            book["price"] = updated_book.price
            return {
                "message": "Book Updated Successfully",
                "book": book
            }
    return {"message": "Book not found"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": f"Book with id {book_id} deleted successfully"}
    return {"message": "Book not found"}
