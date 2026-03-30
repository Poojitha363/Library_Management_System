from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/")
def create_book(title: str, author: str, db: Session = Depends(get_db)):
    return crud.add_book(db, title, author)

@app.post("/members/")
def create_member(name: str, email: str, db: Session = Depends(get_db)):
    return crud.add_member(db, name, email)

@app.post("/issue/")
def issue_book(book_id: int, member_id: int, db: Session = Depends(get_db)):
    return crud.issue_book(db, book_id, member_id)

@app.post("/return/")
def return_book(transaction_id: int, db: Session = Depends(get_db)):
    return crud.return_book(db, transaction_id)
