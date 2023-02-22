import mysql.connector
import os
from mysql.connector import errorcode


def open_connection():
    try:
        connection = mysql.connector.connect(
            username=os.getenv('DB_USERNAME'),
            host=os.getenv('DB_HOST'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB')
        )

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("Successfully connected to PlanetScale")
        return connection


def close_connection(connection):
    connection.close()