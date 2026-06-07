from fastapi import APIRouter, HTTPException
from models import RegisterRequest, LoginRequest 
from utils import hash_password, verify_password, create_token

router = APIRouter()

fake_db ={}

@router.post("/register")
def register(data : RegisterRequest):
    if data.username in fake_db:
        raise HTTPException(status_code=409, detail="Username already exists")
    for user in fake_db.values():
        if data.email == user["email"]:
            raise HTTPException(status_code=409, detail="Email already exists")
    hashed = hash_password(data.password)
    fake_db[data.username] = {
        "password": hashed,
        "email": data.email
    }
    return {"message": data.username + " is registered!"} 

@router.post("/login")
def login(login: LoginRequest):
    if login.username not in fake_db:
        raise HTTPException(status_code=404, detail="Username not registered")
    username_details = fake_db.get(login.username)
    hashed_details = username_details["password"]
    if not hashed_details or not verify_password(login.password, hashed_details):
        raise HTTPException(status_code=401, detail="Invalid credentials!")
    token = create_token({"sub": login.username})
    return {"access_token": token} 
    