from fastapi import APIRouter, HTTPException
from schema import ReviewInfo
from routes import books

router = APIRouter()

fake_review_db = {}

@router.post("/givereview/{bookname}")
def givereview(bookname: str,data: ReviewInfo):
    if bookname not in books.fake_book_db:
        raise HTTPException(status_code=404, detail="Book doesnt exist")
    fake_review_db[bookname] = {
        "rating": data.rating,
        "review": data.review
    }
    return {"message": "Review is added!"}

@router.get("/showreview")
def showreview():
    return fake_review_db

@router.get("/showreview/{bookname}")
def showreview_bookname(bookname: str):
    if bookname in fake_review_db:
        return fake_review_db[bookname]
    else:
        raise HTTPException(status_code=404, detail="Book doesnt exist")
    
@router.delete("/deletereview/{bookname}")
def deletereview(bookname: str):
    if bookname in fake_review_db:
        fake_review_db.pop(bookname)
    else:
        raise HTTPException(status_code=404, detail="Book doesnt exist")
    return {"message": bookname + " review is removed!"}