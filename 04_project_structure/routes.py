from fastapi import APIRouter
from models import Book
from database import books

router = APIRouter()


@router.post("/books")
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