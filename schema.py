from pydantic import BaseModel, Field

class RegisterRequest(BaseModel):
    email: str
    username: str
    password: str
    
class LoginRequest(BaseModel):
    username: str
    password: str
    
class BookInfo(BaseModel):
    bookname: str
    author: str
    genre: str
    
class ReviewInfo(BaseModel):
    rating: int = Field(ge=0, le=5)
    review: str