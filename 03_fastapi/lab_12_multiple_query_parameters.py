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
def get_books(
    author: str | None = None,
    price: int | None = None
):
    filtered_books = []

    for book in books:
        match = True

        if author is not None and book["author"] != author:
            match = False

        if price is not None and book["price"] != price:
            match = False

        if match:
            filtered_books.append(book)

    return {
        "message": "Books retrieved successfully",
        "filters": {
            "author": author,
            "price": price
        },
        "books": filtered_books
    }