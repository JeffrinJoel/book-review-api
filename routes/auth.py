from fastapi import APIRouter, HTTPException, Depends
from schema import RegisterRequest, LoginRequest 
from utils import hash_password, verify_password, create_token
from sqlalchemy.orm import Session
from database import get_db
from models import User

router = APIRouter()

@router.post("/register")
def register(data : RegisterRequest, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == data.username).first():
        raise HTTPException(status_code=409, detail="Username already exists")
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=409, detail="Email already exists")
    hashed = hash_password(data.password)
    new_user = User(username = data.username, email = data.email, password = hashed)
    db.add(new_user)
    db.commit()
    return {"message": data.username + " is registered!"} 

@router.post("/login")
def login(login: LoginRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == login.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Username not registered")
    if not verify_password(login.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials!")
    token = create_token({"sub": login.username})
    return {"access_token": token} 
    