import mysql.connector
import os
import dotenv

def addReadings(sensor_id, formatted_dates_vals, mydb, cursor):

    sql = f"INSERT INTO READINGS_FOR_{sensor_id} (READING_DATE, READING_TIME, VALUE) VALUES (%s, %s, %s)"
    cursor.executemany(sql, formatted_dates_vals)
    mydb.commit()