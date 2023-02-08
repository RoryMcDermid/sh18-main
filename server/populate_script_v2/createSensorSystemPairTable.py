import mysql.connector

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "password",
  database = "moxie_energy"
)

cursor = mydb.cursor( buffered=True)
cursor.execute("DROP TABLE IF EXISTS SENSOR_SYSTEM_PAIRS")
mydb.commit()
cursor.execute("""CREATE TABLE SENSOR_SYSTEM_PAIRS(
                 SENSOR_ID VARCHAR(10) NOT NULL,
                 SYSTEM_ID VARCHAR(10) NOT NULL
            )""")
mydb.commit()

cursor.execute("SELECT SYSTEM_ID FROM SYSTEMS")

system_ids = [x[0] for x in cursor.fetchall()]
for system_id in system_ids:
    cursor.execute(f"SELECT SENSOR_ID FROM SENSORS_FOR_{system_id}")
    sensor_ids = [x[0] for x in cursor.fetchall()]
    for sensor_id in sensor_ids:
        sql = "INSERT IGNORE INTO SENSOR_SYSTEM_PAIRS (SENSOR_ID, SYSTEM_ID) VALUES (%s, %s)"
        cursor.execute(sql, (sensor_id, system_id))
mydb.commit()