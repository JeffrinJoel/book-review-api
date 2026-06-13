from fastapi import APIRouter, HTTPException, Depends
from schema import ReviewInfo
from sqlalchemy.orm import Session
from database import get_db
from models import Review, Book

router = APIRouter()

@router.post("/givereview/{bookname}")
def givereview(bookname: str, data: ReviewInfo, db: Session = Depends(get_db)):
    if not db.query(Book).filter(Book.bookname == bookname).first():
        raise HTTPException(status_code=404, detail="Book doesnt exist")
    review_book = Review(bookname = bookname, rating = data.rating,review = data.review)
    db.add(review_book)
    db.commit()
    return {"message": "Review is added!"}

@router.get("/showreview")
def showreview(db: Session = Depends(get_db)):
    return db.query(Review).all()

@router.get("/showreview/{bookname}")
def showreview_bookname(bookname: str, db: Session = Depends(get_db)):
    review = db.query(Review).filter(Review.bookname == bookname).all()
    if not review:
        raise HTTPException(status_code=404, detail="Book doesnt exist")
    else:
        return review
    
@router.delete("/deletereview/{bookname}")
def deletereview(bookname: str, db: Session = Depends(get_db)):
    review = db.query(Review).filter(Review.bookname == bookname).first()
    if review:
        db.delete(review)
        db.commit()
    else:
        raise HTTPException(status_code=404, detail="Book doesnt exist")
    return {"message": bookname + " review is removed!"}