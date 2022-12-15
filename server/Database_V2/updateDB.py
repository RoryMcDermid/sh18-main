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

system_id = 2542

def update_db(system_id):
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "moxie_energy"
    )

    cursor = mydb.cursor()
    cursor.execute(f"SELECT SENSOR_ID FROM SENSORS_FOR_{system_id}")
    sensor_id_list = list(map(lambda x: x[0], cursor.fetchall()))
    
    cursor.execute(f"SELECT * FROM ITER_1_{sensor_id_list[0]} ORDER BY DATE_OF_RECORD")

    already_stored = cursor.fetchall()
    most_recent_record_date = already_stored[-1][0]
    current_date = datetime.now() 

    readings_from_dates = getDatafromDates(most_recent_record_date, current_date, system_id, sensor_id_list)[0]

    current_sensor = 0
    old_date = readings_from_dates[0]["date"]
    for result in readings_from_dates:
        
        date, reading = result["date"], result["reading"]
        if date < old_date:
            current_sensor += 1
            print("change")
        old_date = date
        sensor_id = sensor_id_list[current_sensor]
        sql = f"INSERT INTO ITER_1_{sensor_id} (DATE_OF_RECORD,VALUE) VALUES(%s, %s)"
        vals = (date, reading)
        cursor.execute(sql, vals)
    mydb.commit()

    iter_list = ["ITER_2", "ITER_3", "ITER_4"]
    # Loop through each possible iteration, passing what one you are working on into a separate function.
    for sensor_id_val in sensor_id_list:
        for iter_val in iter_list:
            pushDownIteration(iter_val, sensor_id_val)
        for iter_val in iter_list:
            deleteFromIter(iter_val, sensor_id_val)
        deleteFromIter("ITER_1", sensor_id)

update_db(system_id)