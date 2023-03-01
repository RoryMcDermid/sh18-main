import psycopg2
import datetime as dt
from helpers.updateFromDates import *
import os
from dotenv import load_dotenv

load_dotenv()


def setupNewCRTables(systems_with_list_of_sensors):
    conn = psycopg2.connect(os.getenv("CONNECTION_STRING"))
    cursor = conn.cursor()

    start_date = dt.datetime.strptime("2022-06-30T23:59:00", "%Y-%m-%dT%H:%M:%S") + dt.timedelta(hours=1)
    end_date = start_date + dt.timedelta(days=3)

    systems_with_list_of_sensors = {2417: ["6311345", "6311346", "6313033", "6313133"]}

    for system in systems_with_list_of_sensors.keys():
        for sensor in systems_with_list_of_sensors[system]:
            cursor.execute(
                f"""CREATE TABLE READINGS_FOR_{sensor}(
                                    READING_DATE DATE NOT NULL,
                                    READING_TIME TIME NOT NULL, 
                                    VALUE DECIMAL(15,6) NOT NULL)"""
            )
            conn.commit()

    updateFromDates(start_date, end_date, systems_with_list_of_sensors, conn, cursor)
