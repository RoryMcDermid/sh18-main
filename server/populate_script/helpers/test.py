import mysql.connector
import datetime as dt


mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "password",
  database = "moxie_energy"
)
cursor = mydb.cursor( buffered=True)

time = dt.datetime.now().time()
print(time)

sql = f"""SELECT BASELINE, AVERAGE FROM FEATURES_FOR_6311346
            WHERE TIME_SLOT = '10:00:00' """
cursor.execute(sql)
current_vals = cursor.fetchall()
baseline = current_vals[0][0]
avg = current_vals[0][1]
print(baseline, avg)