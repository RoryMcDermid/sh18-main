import mysql.connector
from datetime import datetime
import datetime as dt


def deleteFromIter(iter_val):
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "moxie_energy"
    )

    cursor = mydb.cursor()

    time_now = datetime.now()

    if(iter_val == "ITER_1"):
        #time_limit = datetime.strptime((time_now - dt.timedelta(weeks=2)), "%Y-%m-%dT%H:%M:%S")
        time_limit = time_now - dt.timedelta(weeks=2)
    elif(iter_val == "ITER_2"):
        time_limit = (time_now - dt.timedelta(weeks=8))
    elif(iter_val == "ITER_3"):
        time_limit = (time_now - dt.timedelta(weeks=32))
    else:
        return 0

    to_edit = (iter_val + "_6311171").lower()

    sql = f'''
        DELETE FROM {to_edit}
        WHERE DATE_OF_RECORD < %s    
        '''
    cursor.execute(sql, (time_limit, ))
    mydb.commit()

    
deleteFromIter("ITER_1")

    
    

