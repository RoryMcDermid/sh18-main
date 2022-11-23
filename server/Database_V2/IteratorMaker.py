import mysql.connector
from Get24hrData import *
from datetime import datetime

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "password",
  database = "moxie_energy"
)

cursor = mydb.cursor()

sensor_id ="6311171"#input("Which sensor would you like yesterday's 24hr data for?")

cursor.execute(f'''SELECT * FROM ITER_1_{sensor_id}''')

results = cursor.fetchall()

cursor.execute(f"DROP TABLE IF EXISTS ITER_2_{sensor_id}")
position = 0

cursor.execute("SHOW TABLES")



tables = []
for x in cursor:
  tables.append(x[0])



if "iter_2_6311171" not in tables:
  
  sql =f'''CREATE TABLE ITER_2_{sensor_id}(
    DATE_OF_RECORD DATETIME NOT NULL PRIMARY KEY,
    VALUE DECIMAL(9,6) NOT NULL
    )'''
  cursor.execute(sql)

for vals in results:

  if(position % 2 == 0):
    date = vals[0]
    sum_of_vals = vals[1] + results[position + 1][1]
    sql = f"INSERT INTO ITER_2_{sensor_id} (DATE_OF_RECORD,VALUE) VALUES(%s, %s)"
    vals = (date, sum_of_vals)
    cursor.execute(sql, vals)
  position += 1

mydb.commit()