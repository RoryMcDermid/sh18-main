import mysql.connector
from datetime import datetime
import datetime as dt
from helpers.getDataFromDates import *
from helpers.pushDownIteration import *
from deleteFromIter import *

#This file brings it all together. It finds the date of the most recently stored value in the 
#iter_1 table, then gets all the dates from the api using the previously defined function.
#It then performs the push down function, adding all appropriate values to tables that are
#needed. Then remove the unwanted values from tables that are no longer needed to be stored.

sensor_id = 1234

def update_db(sensor_id):
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "moxie_energy"
    )

    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM ITER_1_{sensor_id} ORDER BY DATE_OF_RECORD")

    already_stored = cursor.fetchall()
    most_recent_record_date = already_stored[-1][0]
    current_date = datetime.now()

    readings_from_dates = getDatafromDates(most_recent_record_date, current_date)

    for result in readings_from_dates:
    
        date, reading = result["date"], result["reading"]
        sql = f"INSERT INTO ITER_1_{sensor_id} (DATE_OF_RECORD,VALUE) VALUES(%s, %s)"
        vals = (date, reading)
        cursor.execute(sql, vals)
    mydb.commit()

    iter_list = ["ITER_2", "ITER_3", "ITER_4"]
    # Loop through each possible iteration, passing what one you are working on into a separate function.
    for iter_val in iter_list:
        pushDownIteration(iter_val)
    for iter_val in iter_list:
        deleteFromIter(iter_val)
    deleteFromIter("ITER_1")

update_db(sensor_id)