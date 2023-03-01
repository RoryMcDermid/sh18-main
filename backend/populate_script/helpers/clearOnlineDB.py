import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()
mydb = psycopg2.connect(os.getenv("CONNECTION_STRING"))
cursor = mydb.cursor()
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()

for val in tables:
    cursor.execute("DROP TABLE " + val[1] + ";")
mydb.commit()
