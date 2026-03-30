from sqlalchemy.orm import Session
from models import Book, Member, Transaction
from datetime import date

def add_book(db: Session, title: str, author: str):
    book = Book(title=title, author=author)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def add_member(db: Session, name: str, email: str):
    member = Member(name=name, email=email)
    db.add(member)
    db.commit()
    db.refresh(member)
    return member

def issue_book(db: Session, book_id: int, member_id: int):
    book = db.query(Book).filter(Book.id == book_id, Book.available == 1).first()
    if not book:
        return None
    book.available = 0
    transaction = Transaction(book_id=book_id, member_id=member_id, issue_date=date.today())
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def return_book(db: Session, transaction_id: int):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if transaction and not transaction.return_date:
        transaction.return_date = date.today()
        transaction.book.available = 1
        db.commit()
        db.refresh(transaction)
    return transaction
