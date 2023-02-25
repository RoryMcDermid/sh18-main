import mysql.connector
import datetime as dt
from helpers.addDataFromDates import *
from helpers.createSensorsForSystem import *
from helpers.createDB import *
from helpers.createSystems import *
import os
import dotenv

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
dotenv.load_dotenv(dotenv_path=env_path)

mydb = mysql.connector.connect(
    username=os.environ.get('DB_USERNAME'),
    host=os.environ.get('DB_HOST'),
    password=os.environ.get('DB_PASSWORD'),
    database=os.environ.get('DB')
)
cursor = mydb.cursor(buffered=True)

system_ids = create_systems(mydb, cursor)

system_call_mock = dict(json.load(open("mocks/system_ids.json")))
sensors_mock = dict(json.load(open("mocks/getSensors.json")))

system_ids = create_systems(mydb, cursor, mock=system_call_mock, online=True)
systems_with_list_of_sensors = get_systems_sensor_list(
    system_ids, mydb, cursor, online=True)

today = dt.date.today()
setup_end_date = dt.datetime.combine(today, dt.datetime.min.time()) - dt.timedelta(minutes=1)
setup_start_date = setup_end_date - dt.timedelta(days=1)

addDatafromDates(setup_start_date, setup_end_date,
                 systems_with_list_of_sensors, mydb, cursor, True)
