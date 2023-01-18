import mysql.connector
import datetime as dt
from helpers.getDataFromDates import *
from helpers.pushDownIteration import *
from helpers.createSensorsForSystem import *
from helpers.createDB import *
from helpers.createSystems import *


mydb = mysql.connector.connect(
  host = "aws-eu-west-2.connect.psdb.cloud",
  user = "zjalycxffixqot7bqc0t",
  password = "pscale_pw_hwoKJMYQbyNjTwgWlSUfZnTY47t7PlC8b08Bgk4V27z",
  database = "test-db-v3"
)


cursor = mydb.cursor()

cursor.execute('''CREATE TABLE test (field_1);''')

mydb.commit()


# system_ids = create_systems(mydb, cursor)

# return a dictionary where the keys are the system ids, and
# the values are the sensors associated with that system

# systems_with_sensors_dict = get_systems_sensor_list_online(system_ids, mydb, cursor)
# systems_with_sensors_dict.pop(2542)





