import mysql.connector
import os
import dotenv

def addReadings(sensor_id, formatted_dates_vals, mydb, cursor, online):
    if online:
        env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
        dotenv.load_dotenv(dotenv_path=env_path)

        mydb = mysql.connector.connect(
                        username=os.environ.get('DB_USERNAME'),
                        host=os.environ.get('DB_HOST'),
                        password=os.environ.get('DB_PASSWORD'),
                        database=os.environ.get('DB')
                    )
        cursor = mydb.cursor(buffered=True)
    sql = f"INSERT IGNORE INTO READINGS_FOR_{sensor_id} (READING_DATE, VALUE) VALUES (%s, %s)"
    cursor.executemany(sql, formatted_dates_vals)
    mydb.commit()