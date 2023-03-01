import psycopg2
from helpers.updateFromDates import *

def crClearTables(systems_with_list_of_sensors):
    connection_string = "postgresql://moxie:iYmwQU_OL2HI1-fiiOqSuQ@fooled-dolphin-7094.8nj.cockroachlabs.cloud:26257/moxie_data?sslmode=verify-full"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    for system in systems_with_list_of_sensors.keys():
        for sensor in systems_with_list_of_sensors[system]:
            cursor.execute(f"DROP TABLE IF EXISTS public.READINGS_FOR_{sensor}")
            conn.commit()
    cursor.close()
    conn.close()