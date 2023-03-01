import os
from dotenv import load_dotenv
import psycopg2
import datetime as dt
from helpers.updateFromDates import *

load_dotenv()


def addFollowingDays(systems_with_list_of_sensors):
    conn = psycopg2.connect(os.getenv("CONNECTION_STRING"))
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM READINGS_FOR_6313133 ORDER BY(READING_DATE) DESC")
    row_for_start = cursor.fetchone()

    start_date = dt.datetime.combine(row_for_start[0], row_for_start[1])
    end_date = start_date + dt.timedelta(days=4)

    # systems_with_list_of_sensors = {2417: ['6311345', '6311346', '6313033', '6313133']}
    if end_date > dt.datetime.now():
        end_date = dt.datetime.now() - dt.timedelta(minutes=15)

    updateFromDates(start_date, end_date, systems_with_list_of_sensors, conn, cursor)


addFollowingDays({2417: ["6311345", "6311346", "6313033", "6313133"]})
