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
system_id = "2542"#input("What system does this belong to?")

cursor.execute(f"DROP TABLE IF EXISTS ITER1_{sensor_id}")

sql =f'''CREATE TABLE ITER_1_{sensor_id}(
   DATE_OF_RECORD DATETIME NOT NULL PRIMARY KEY,
   VALUE DECIMAL(9,6) NOT NULL
)'''
cursor.execute(sql)

data24hr = get24hrData(sensor_id, system_id)

parsed_24hr_data = []
parsed_record_datetimes = []


for i in range(len(data24hr["systems"][0]["sensors"][0]["data"])):
  parsed_value = list(data24hr["systems"][0]["sensors"][0]["data"][i]["values"].values())[0]
  parsed_timestamp = datetime.strptime(data24hr["systems"][0]["sensors"][0]["data"][i]["record_date"][:19], "%Y-%m-%dT%H:%M:%S")

  sql = f"INSERT INTO ITER_1_{sensor_id} (DATE_OF_RECORD,VALUE) VALUES(%s, %s)"
  vals = (parsed_timestamp, parsed_value)
  cursor.execute(sql, vals)
mydb.commit()

