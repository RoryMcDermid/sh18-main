import mysql.connector
import os
import dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
dotenv.load_dotenv(dotenv_path=env_path)

mydb = mysql.connector.connect(
     username=os.environ.get('DB_USERNAME'),
     host=os.environ.get('DB_HOST'),
     password=os.environ.get('DB_PASSWORD'),
     database=os.environ.get('DB')
      )
cursor = mydb.cursor(buffered=True)

cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()
sql = ""
for val in tables:
    if val[0] != "SYSTEMS":
        sql += val[0] + ","
    else:
        sql += val[0]

cursor.execute("DROP TABLE " + sql +";")
mydb.commit()