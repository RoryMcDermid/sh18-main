import mysql.connector

def create_db():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
  )

  

  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE moxie_energy")
