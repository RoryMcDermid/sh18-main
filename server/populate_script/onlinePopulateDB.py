import mysql.connector
import datetime as dt
from helpers.addDataFromDates import *
from helpers.pushDownIteration import *
from helpers.createSensorsForSystem import *
from helpers.createDB import *
from helpers.createSystems import *

TIME_PERIOD = 2
mydb = mysql.connector.connect(
        username = "wod2dh1e3jfuxs210ykt",
        host = "aws-eu-west-2.connect.psdb.cloud",
        password = "pscale_pw_zAx3LdXNX0R0YVevbMphKOEjXcSVMc1BKe5PfaCDDB2",
        database = "moxie_live"
        )
cursor = mydb.cursor(buffered=True)
system_ids = create_systems(mydb, cursor)

system_call_mock = dict(json.load(open("mocks/system_ids.json")))
sensors_mock = dict(json.load(open("mocks/getSensors.json")))

# creates the SYSTEMS table in the db that stores the system_id and
# the name of that system. Returns a list of the system ids as integers.
system_ids = create_systems(mydb, cursor, mock=system_call_mock, online=True)

# Creates the SENSORS_FOR_{system id} tables that store the 
# sensor_id, system_id and sensor_measurement. The sensor measurement
# is stored as it is needed for parsing a returned json later on.
# This function also contains validity checks so that a sensor is only
# added to one specific system even if it belongs to two, and if a system has
# no associated unique sensors it is removed from the SYSTEMS table. 
# Returned is a dictionary that has the system ids as the keys, and unique
# sensor_ids as the values stored in a list
systems_with_list_of_sensors = get_systems_sensor_list(system_ids, mydb, cursor, online=True)

# Setup the dates that we are looking to record from.
# This takes yesterday as the most recent date and goes 2 days back from there
# to get the data from.
# The reasom for ending at yesterday is to allow for the updateDB.py file to be called to
# show that it is working.

setup_end_date = dt.datetime.now() 
setup_start_date = setup_end_date - dt.timedelta(hours=1)

addDatafromDates(setup_start_date, setup_end_date, systems_with_list_of_sensors, mydb, cursor, True)





