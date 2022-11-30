import mysql.connector
from datetime import datetime
import datetime as dt
from getDataFromDates import *
from pushDownIteration import *

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "password",
  database = "moxie_energy"
)

cursor = mydb.cursor()

setup_end_date = datetime.now() - dt.timedelta(days=1)
setup_start_date = setup_end_date - dt.timedelta(weeks=2)
readings_from_dates = getData(setup_start_date, setup_end_date)

cursor.execute(f"DROP TABLE IF EXISTS ITER_1_6311171")

sql =f'''CREATE TABLE ITER_1_6311171(
   DATE_OF_RECORD DATETIME NOT NULL PRIMARY KEY,
   VALUE DECIMAL(9,6) NOT NULL
)'''
cursor.execute(sql)

for result in readings_from_dates:
    
    date, reading = result["date"], result["reading"]
    sql = f"INSERT INTO ITER_1_6311171 (DATE_OF_RECORD,VALUE) VALUES(%s, %s)"
    vals = (date, reading)
    cursor.execute(sql, vals)
mydb.commit()

iter_list = ["ITER_2", "ITER_3", "ITER_4"]
# Loop through each possible iteration, passing what one you are working on into a separate function.
for iter_val in iter_list:
    pushDownIteration(iter_val)







