
import json, math
from db import conn, cursor

def clean_number(v):
    if v is None:
        return None
    if isinstance(v, (int, float)) and math.isnan(v):
        return None
    return v

with open("US_recipes_null.Pdf.json") as f:
    data = json.load(f)

for r in data.values():
    cursor.execute(
        '''
        INSERT INTO recipes
        (cuisine, title, rating, prep_time, cook_time, total_time, description, nutrients, serves)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ''',
        (
            r.get("cuisine"),
            r.get("title"),
            clean_number(r.get("rating")),
            clean_number(r.get("prep_time")),
            clean_number(r.get("cook_time")),
            clean_number(r.get("total_time")),
            r.get("description"),
            json.dumps(r.get("nutrients")),
            r.get("serves"),
        )
    )

conn.commit()
cursor.close()
conn.close()

print("Data loaded successfully")
