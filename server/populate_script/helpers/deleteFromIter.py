import mysql.connector
from datetime import datetime
import datetime as dt


def deleteFromIter(sensor_id, iter_val, mydb, cursor, online):

    if online:
        mydb = mysql.connector.connect(
                        username = "wod2dh1e3jfuxs210ykt",
                        host = "aws-eu-west-2.connect.psdb.cloud",
                        password = "pscale_pw_zAx3LdXNX0R0YVevbMphKOEjXcSVMc1BKe5PfaCDDB2",
                        database = "moxie_live"
                        )
        cursor = mydb.cursor(buffered=True)

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

    

    
    

