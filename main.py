from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from db import cursor

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"message": "Recipe API is running"}

@app.get("/api/recipes")
def get_recipes(page: int = 1, limit: int = 10):
    offset = (page - 1) * limit
    cursor.execute(
        '''
        SELECT * FROM recipes
        ORDER BY rating DESC NULLS LAST
        LIMIT %s OFFSET %s
        ''',
        (limit, offset),
    )
    return {"page": page, "limit": limit, "data": cursor.fetchall()}

@app.get("/api/recipes/search")
def search(
    title: str = None,
    cuisine: str = None,
    rating: float = None,
    total_time: int = None,
):
    query = "SELECT * FROM recipes WHERE 1=1"
    params = []

    if title:
        query += " AND title ILIKE %s"
        params.append(f"%{title}%")
    if cuisine:
        query += " AND cuisine=%s"
        params.append(cuisine)
    if rating:
        query += " AND rating>=%s"
        params.append(rating)
    if total_time:
        query += " AND total_time<=%s"
        params.append(total_time)

    cursor.execute(query, params)
    return {"data": cursor.fetchall()}