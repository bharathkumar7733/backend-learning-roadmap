from pydantic import BaseModel


class Book(BaseModel):
    bookname: str
    author: str
    price: int