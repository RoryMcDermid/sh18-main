import os
from dotenv import load_dotenv
import psycopg2
import datetime as dt

conn = psycopg2.connect(os.getenv("CONNECTION_STRING"))
cursor = conn.cursor()

cursor.execute(f"SELECT * FROM READINGS_FOR_6311171 ORDER BY (READING_DATE) DESC")
print(cursor.fetchone())
cursor.close()
conn.close()
