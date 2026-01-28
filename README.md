
# Recipe API Project (Beginner Friendly)

## What this project does
- Loads recipe data from JSON
- Stores it in PostgreSQL
- Exposes REST APIs using FastAPI

## How to run (VERY IMPORTANT)
1. Install Python 3.10+
2. Install PostgreSQL
3. Create database:
   CREATE DATABASE recipes_db;

4. Update db.py with your DB password
5. Install dependencies:
   pip install -r requirements.txt

6. Load data:
   python load_data.py

7. Run API:
   uvicorn main:app --reload

Open browser:
http://127.0.0.1:8000/docs
