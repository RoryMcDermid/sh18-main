from database import open_connection, close_connection


def get_all_systems():
    mydb = open_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM SYSTEMS")
    systems = cursor.fetchall()
    cursor.close()
    close_connection(mydb)
    return systems
