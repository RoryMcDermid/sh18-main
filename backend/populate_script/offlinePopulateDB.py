import mysql.connector
import datetime as dt
from helpers.createSensorsForSystem import *
from helpers.createDB import *
from helpers.createSystems import *
from helpers.addDataFromDates import *
import json

TIME_PERIOD = 2
create_db()

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "password",
  database = "moxie_energy"
)

cursor = mydb.cursor( buffered=True)

system_call_mock = dict(json.load(open("mocks/system_ids.json")))
sensors_mock = dict(json.load(open("mocks/getSensors.json")))

# Creates the SYSTEMS table in the db that stores the system_id and
# the name of that system. Returns a list of the system ids as integers.
# As part of our testing process, a mock was created to limit the calls
# to the API to avoid timeouts.
system_ids = create_systems(mydb, cursor,)

# Creates the SENSORS_FOR_{system id} tables that store the 
# sensor_id, system_id and sensor_measurement. The sensor measurement
# is stored as it is needed for parsing a returned json later on.
# This function also contains validity checks so that a sensor is only
# added to one specific system even if it belongs to two, and if a system has
# no associated unique sensors it is removed from the SYSTEMS table. 
# Returned is a dictionary that has the system ids as the keys, and unique
# sensor_ids as the values stored in a list
systems_with_list_of_sensors = get_systems_sensor_list(system_ids, mydb, cursor, mock = sensors_mock)

# Setup the dates that we are looking to record from.
# This takes yesterday as the most recent date and goes 2 days back from there
# to get the data from.
# The reason for ending at yesterday is to allow for the updateDB.py file to be called to
# show that it is working.

today = dt.date.today()
setup_end_date = dt.datetime.combine(today, dt.datetime.min.time()) - dt.timedelta(minutes=1) - dt.timedelta(weeks=4)
setup_start_date = setup_end_date - dt.timedelta(weeks=4)

addDatafromDates(setup_start_date, setup_end_date, systems_with_list_of_sensors, mydb, cursor)