import mysql.connector
import datetime
#The way this function is currently set up is only for the initial populate script call.
#Depending on the iter_val passed, it evaluates the values stored in the table that comes before it
# and then adds the appropriate compressed vals to its own table.
#The function currently drops and creates new tables each time, of course it will have to be modified
#to eventually add and remove values from its table depending on how long we wish to store te data.
#An easy change, but of course nice to get the first population script with static vals set up.

def pushDownIteration(iter_val, sensor_id, mydb, cursor, online=False):
    if online:
        mydb = mysql.connector.connect(
            username = "wod2dh1e3jfuxs210ykt",
            host = "aws-eu-west-2.connect.psdb.cloud",
            password = "pscale_pw_zAx3LdXNX0R0YVevbMphKOEjXcSVMc1BKe5PfaCDDB2",
            database = "moxie_live"
        )
        cursor = mydb.cursor(buffered=True)

#Depending on the iter_val, select from previous table.
    cursor.execute(f"SELECT * FROM {iter_val}_{sensor_id} ORDER BY(DATE_OF_RECORD) DESC")
    try:
        most_recent_record_date = cursor.fetchone()[0]
        if(iter_val == "ITER_2"):
            cursor.execute(f"SELECT * FROM ITER_1_{sensor_id} WHERE DATE_OF_RECORD > %s", (most_recent_record_date,))
        elif(iter_val == "ITER_3"):
            cursor.execute(f"SELECT * FROM ITER_2_{sensor_id} WHERE DATE_OF_RECORD > %s", (most_recent_record_date,))
        else:
            cursor.execute(f"SELECT * FROM ITER_3_{sensor_id} WHERE DATE_OF_RECORD > %s", (most_recent_record_date,))

        previous_iter_vals = cursor.fetchall()
        to_edit = (iter_val + '_' + sensor_id).upper()

        #If we want hourly or 4-hourly vals, do modulo 4, if its going from 4-hour to day, modulo 6.
        if(iter_val == "ITER_2" or iter_val == "ITER_3"):
            modulo_val = 4
        else:
            modulo_val = 6   
        count = 0
        backlog = 0.0
            
        for val in previous_iter_vals:
            #count begins at 1 to allow modulo to work, no zero-indexing here!
            count += 1
            if(count % modulo_val != 0):
                backlog += float(val[1])
            else:
                if online:
                    mydb = mysql.connector.connect(
                        username = "wod2dh1e3jfuxs210ykt",
                        host = "aws-eu-west-2.connect.psdb.cloud",
                        password = "pscale_pw_zAx3LdXNX0R0YVevbMphKOEjXcSVMc1BKe5PfaCDDB2",
                        database = "moxie_live"
                        )
                    cursor = mydb.cursor(buffered=True)
                backlog += float(val[1])
                sql = f"INSERT IGNORE INTO {to_edit} (DATE_OF_RECORD,VALUE) VALUES(%s, %s)"
                vals = (val[0], backlog)
                cursor.execute(sql, vals)
                backlog = 0.0
                mydb.commit()
    except:
        return True
   
    return True






    
    

