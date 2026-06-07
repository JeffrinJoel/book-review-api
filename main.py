from fastapi import FastAPI
from routes import auth,books,reviews

app = FastAPI()
app.include_router(auth.router)
app.include_router(books.router)
app.include_router(reviews.router)