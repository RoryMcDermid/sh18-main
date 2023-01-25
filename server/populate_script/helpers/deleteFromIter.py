import mysql.connector
from datetime import datetime
import datetime as dt


def deleteFromIter(sensor_id, iter_val, mydb, cursor):

    time_now = datetime.now()

    if(iter_val == "ITER_1"):
        time_limit = (time_now - dt.timedelta(days=2)).strftime( "%Y-%m-%dT%H:%M:%S")
    elif(iter_val == "ITER_2"):
        time_limit = (time_now - dt.timedelta(weeks=1)).strftime( "%Y-%m-%dT%H:%M:%S")
    elif(iter_val == "ITER_3"):
        time_limit = (time_now - dt.timedelta(weeks=4)).strftime( "%Y-%m-%dT%H:%M:%S")
    else:
        return 0

    to_edit = (iter_val + "_" + sensor_id).upper()

    sql = f'''
        DELETE FROM {to_edit}
        WHERE DATE_OF_RECORD < %s    
        '''
    cursor.execute(sql, (time_limit, ))
    mydb.commit()

    

    
    

