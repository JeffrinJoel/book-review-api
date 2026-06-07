from fastapi import APIRouter, HTTPException
from models import BookInfo

router = APIRouter()

fake_book_db = {}

@router.post("/addbook")
def addbook (data: BookInfo):
    if data.bookname in fake_book_db:
        raise HTTPException(status_code=409, detail="The book already exists")
    fake_book_db[data.bookname] = {
        "author" : data.author,
        "genre" : data.genre
    }
    return {"message": data.bookname + " is successfully added!"}

@router.get("/books")
def books ():
    return fake_book_db

@router.get("/book/{bookname}")
def singlebook(bookname: str):
    if bookname not in fake_book_db:
        raise HTTPException(status_code=404, detail="Book not present")
    return fake_book_db[bookname]

@router.delete("/removebook/{bookname}")
def removbook(bookname: str):
    if bookname not in fake_book_db:
        raise HTTPException(status_code=404, detail="Book doesnt exist")
    fake_book_db.pop(bookname)
    return {"message": bookname + " is removed!"}