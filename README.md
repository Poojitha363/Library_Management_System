# Library_Management_System

A simple Library Management System built with FastAPI and SQLite.
This project provides REST APIs to manage books, members, and transactions (issue/return).
It demonstrates clean backend design, secure password storage, and database integration.

# Features
1.Add, update, delete, and search books
2.Manage library members
3.Issue and return books with due dates
4.Track availability status
5.REST API with interactive docs 

# Tech Stack
1.Python 3.9+
2.FastAPI (backend framework)
3.SQLite (database)

# Project Structure 
library_management/
│── main.py          # FastAPI app
│── models.py        # Database models
│── database.py      # DB connection
│── crud.py          # CRUD operations
│── requirements.txt # Dependencies

# Setup Instructions
1.Clone the repository:
git clone https://github.com/your-username/library-management.git
cd library-management

2.Create a virtual environment:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3.Install dependencies:
pip install -r requirements.txt

4.Run the server:
uvicorn main:app --reload

5.Open API docs:
http://127.0.0.1:8000/docs

# Future Improvements
JWT authentication for secure sessions
Role-based access (Admin vs Member)
Reporting (overdue books, usage stats)
Docker setup for deployment

# Author
Poojitha Indirala
BTECH CSE in NIT WARANGAL
Interested in backend systems, AI applications, and scalable software engineering.


