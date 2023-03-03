from database import open_connection, close_connection


def get_all_readings_for_sensor(sensorid):
    mydb = open_connection()
    cursor = mydb.cursor()
    cursor.execute(
        f"SELECT * FROM READINGS_FOR_{sensorid}"
    )
    readings = cursor.fetchall()
    cursor.close()
    close_connection(mydb)
    return readings
