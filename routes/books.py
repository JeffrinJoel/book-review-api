from fastapi import APIRouter, HTTPException, Depends
from schema import BookInfo
from sqlalchemy.orm import Session
from database import get_db
from models import Book

router = APIRouter()

@router.post("/addbook")
def addbook (data: BookInfo, db: Session = Depends(get_db)):
    if db.query(Book).filter(Book.bookname == data.bookname).first():
        raise HTTPException(status_code=409, detail="The book already exists")
    new_book = Book(bookname = data.bookname, author = data.author, genre = data.genre)
    db.add(new_book)
    db.commit()
    return {"message": data.bookname + " is successfully added!"}

@router.get("/books")
def books (db: Session = Depends(get_db)):
    return db.query(Book).all()

@router.get("/book/{bookname}")
def singlebook(bookname: str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.bookname == bookname).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not present")
    return book

@router.delete("/removebook/{bookname}")
def removbook(bookname: str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.bookname == bookname).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book doesnt exist")
    db.delete(book)
    db.commit()
    return {"message": bookname + " is removed!"}