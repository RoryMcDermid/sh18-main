from database import open_connection, close_connection


def get_sensors_in_system(systemid):
    mydb = open_connection()
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM SENSORS_FOR_{systemid}")
    sensors = cursor.fetchall()
    cursor.close()
    close_connection(mydb)
    return sensors
