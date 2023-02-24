import mysql.connector
import datetime as dt
from helpers.createSensorsForSystem import *
from helpers.createDB import *
from helpers.createSystems import *
from helpers.addDataFromDates import *
import json

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

system_ids = create_systems(mydb, cursor,)
systems_with_list_of_sensors = get_systems_sensor_list(system_ids, mydb, cursor, mock = sensors_mock)

today = dt.date.today()
setup_end_date = dt.datetime.combine(today, dt.datetime.min.time()) - dt.timedelta(minutes=1) - dt.timedelta(weeks=4)
setup_start_date = setup_end_date - dt.timedelta(weeks=4)

addDatafromDates(setup_start_date, setup_end_date, systems_with_list_of_sensors, mydb, cursor)