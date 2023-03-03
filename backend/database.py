import psycopg2
import os
from mysql.connector import errorcode


def open_connection():
    try:
        connection = psycopg2.connect(os.getenv("CONNECTION_STRING"))
        print("connected to database")
        return connection
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")


def close_connection(connection):
    connection.close()
