import mysql.connector

mydb = mysql.connector.connect(
  host = "aws-eu-west-2.connect.psdb.cloud",
  user = "6l7qfm1r0rvho1arc21e",
  password = "pscale_pw_3QmXuV4sTqnRIQmnIjll63RH4qQ8rpPtK2Y7Uda67zW",
  database = "moxie_live"
)


cursor = mydb.cursor()

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