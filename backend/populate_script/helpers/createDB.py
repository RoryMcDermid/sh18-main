import mysql.connector

def create_db():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
  ) 
  mycursor = mydb.cursor()
  try:
    mycursor.execute("CREATE DATABASE moxie_energy")
  except:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="moxie_energy"
  )
    cursor = mydb.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    for table in tables:
      cursor.execute(f"DROP TABLE {table[0]}")
      mydb.commit()