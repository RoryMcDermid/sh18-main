from database import open_connection, close_connection


def get_readings_for_sensors(sensorids, start_date, end_date):
    mydb = open_connection()
    cursor = mydb.cursor()

    readings = []
    for sensorid in sensorids:
        cursor.execute(
            f"SELECT * FROM READINGS_FOR_{sensorid} WHERE READING_DATE>='{start_date}' AND READING_DATE<'{end_date}'"
        )
        readings.append(cursor.fetchall())

    cursor.close()
    close_connection(mydb)

    return readings
