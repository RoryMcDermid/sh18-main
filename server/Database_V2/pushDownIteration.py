import mysql.connector
from datetime import datetime
#The way this function is currently set up is only for the initial populate script call.
#Depending on the iter_val passed, it evaluates the values stored in the table that comes before it
# and then adds the appropriate compressed vals to its own table.
#The function currently drops and creates new tables each time, of course it will have to be modified
#to eventually add and remove values from its table depending on how long we wish to store te data.
#An easy change, but of course nice to get the first population script with static vals set up.
def pushDownIteration(iter_val):

    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "moxie_energy"
    )
    cursor = mydb.cursor()

#Depending on the iter_val, select from previous table.
    if(iter_val == "ITER_2"):
        cursor.execute("SELECT * FROM ITER_1_6311171")
    elif(iter_val == "ITER_3"):
        cursor.execute("SELECT * FROM ITER_2_6311171")
    else:
        cursor.execute("SELECT * FROM ITER_3_6311171")

    previous_iter_vals = cursor.fetchall()
    to_edit = (iter_val + "_6311171").lower()

    cursor.execute(f"DROP TABLE IF EXISTS {to_edit}")
        
        
    sql =f'''CREATE TABLE {to_edit}(
        DATE_OF_RECORD DATETIME NOT NULL PRIMARY KEY,
        VALUE DECIMAL(9,6) NOT NULL
        )'''
    cursor.execute(sql)

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
            sql = f"INSERT INTO {to_edit} (DATE_OF_RECORD,VALUE) VALUES(%s, %s)"
            vals = (val[0], backlog)
            cursor.execute(sql, vals)
            backlog = 0.0
    mydb.commit()






    
    

