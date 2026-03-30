# Library_Management_System
A simple Library Management System built with FastAPI and SQLite.
This project provides REST APIs to manage books, members, and transactions (issue/return).
It demonstrates clean backend design, secure password storage, and database integration.
# Features
Manage books (add, update, delete, search)

Manage members (add, update, delete)

Issue and return books with due dates

Track availability status

REST API with interactive docs

# Tech Stack
Python 3.9+

FastAPI (backend framework)

SQLite (database)

SQLAlchemy (ORM)

bcrypt (password hashing)

# Setup Instructions
1.Clone the repository:
git clone https://github.com/your-username/library_management_system.git
cd library_management_system

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

Role‑based access (Admin vs Member)

Reporting (overdue books, usage stats)

Docker setup for deployment
# Author
Poojitha Indirala  
Final‑year CSE student, NIT Warangal
Interested in backend systems, AI applications, and scalable software engineering.
