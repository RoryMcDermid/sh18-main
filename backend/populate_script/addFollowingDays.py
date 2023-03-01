import psycopg2
import datetime as dt
from helpers.updateFromDates import *

def addFollowingDays(systems_with_list_of_sensors):
    connection_string = "postgresql://moxie:iYmwQU_OL2HI1-fiiOqSuQ@fooled-dolphin-7094.8nj.cockroachlabs.cloud:26257/moxie_data?sslmode=verify-full"
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM READINGS_FOR_6313133 ORDER BY(READING_DATE) DESC")
    row_for_start = cursor.fetchone()

    start_date = dt.datetime.combine(row_for_start[0], row_for_start[1])
    end_date = start_date + dt.timedelta(days=4)

    # systems_with_list_of_sensors = {2417: ['6311345', '6311346', '6313033', '6313133']}
    if end_date > dt.datetime.now():
        end_date = dt.datetime.now() - dt.timedelta(minutes=15)

    updateFromDates(start_date, end_date, systems_with_list_of_sensors, conn, cursor)

addFollowingDays({2417: ['6311345', '6311346', '6313033', '6313133']})