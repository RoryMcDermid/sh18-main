import datetime as dt
from helpers.addDataFromDates import *
from helpers.createSensorsForSystem import *
from helpers.createDB import *
from helpers.createSystems import *
import psycopg2

connection_string = "postgresql://moxie:iYmwQU_OL2HI1-fiiOqSuQ@fooled-dolphin-7094.8nj.cockroachlabs.cloud:26257/moxie_data?sslmode=verify-full"

mydb = psycopg2.connect(connection_string)

cursor = mydb.cursor()

system_call_mock = dict(json.load(open("mocks/system_ids.json")))
sensors_mock = dict(json.load(open("mocks/getSensors.json")))


system_ids = create_systems(mydb, cursor, system_call_mock)
systems_with_list_of_sensors = get_systems_sensor_list(system_ids, mydb, cursor, sensors_mock)

today = dt.date.today()
setup_end_date = dt.datetime.combine(today, dt.datetime.min.time()) - dt.timedelta(minutes=1)
setup_start_date = setup_end_date - dt.timedelta(days=2)

addDatafromDates(setup_start_date, setup_end_date,
                 systems_with_list_of_sensors, mydb, cursor, True)