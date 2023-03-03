import os
from dotenv import load_dotenv
import psycopg2
from helpers.updateFromDates import *

def crClearTables(systems_with_list_of_sensors):
    load_dotenv()
    conn = psycopg2.connect(os.getenv("CONNECTION_STRING"))
    cursor = conn.cursor()

    for system in systems_with_list_of_sensors.keys():
        for sensor in systems_with_list_of_sensors[system]:
            cursor.execute(f"DROP TABLE IF EXISTS public.READINGS_FOR_{sensor}")
            conn.commit()
    cursor.close()
    conn.close()