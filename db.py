
import psycopg2

conn = psycopg2.connect(
    dbname="recipes_db",
    user="postgres",
    password="YOUR PASSWORD",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()
