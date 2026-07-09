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
    },
    {
        "id": 5,
        "bookname": "JavaScript Basics",
        "author": "Brendan",
        "price": 450
    }
]
filtered_books = []

@app.get("/books")
def get_books(author: str):
    """Retrieve list of books filtered by author name."""
    print(f"Searching books for author: {author}")
    filtered_books.clear()
    for book in books:
        if book["author"] == author:
            filtered_books.append(book)
    return filtered_books