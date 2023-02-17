import mysql.connector
from getWholesaleEnergyPrice import *

mydb = mysql.connector.connect(
    username="wod2dh1e3jfuxs210ykt",
    host="aws-eu-west-2.connect.psdb.cloud",
    password="pscale_pw_zAx3LdXNX0R0YVevbMphKOEjXcSVMc1BKe5PfaCDDB2",
    database="moxie_live"
)
cursor = mydb.cursor(buffered=True)

# cursor.execute("SELECT * FROM SYSTEMS")
# all_systems = [x[0] for x in cursor.fetchall()]
all_systems = [2417]
price_data = None

for system in all_systems:
    cursor.execute(f"SELECT SENSOR_ID FROM SENSORS_FOR_{system}")
    #all_sensors = [x[0] for x in cursor.fetchall()]
    all_sensors = [6311171]
    for sensor_id in all_sensors:
        sensor_data = cursor.execute(f"SELECT * FROM READINGS_FOR_{sensor_id}")
        print(sensor_data)

    # ASSUMPTION OF A LIST OF TUPLES EACH WITH A DATE AND A VALUE
        # oldest_date_formatted = dt.datetime.strftime(sensor_data[-1]["READING_DATE"], "%d-%m-%Y")
        # most_recent_date_formatted = dt.datetime.strftime(sensor_data[0]["READING_DATE"], "%d-%m-%Y")
        # if price_data is None:
        #     price_data = getWholesaleEnergyPrice(oldest_date_formatted, most_recent_date_formatted)