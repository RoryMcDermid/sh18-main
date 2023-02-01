import mysql.connector
def addToIter(sensor_id, iter_val, formatted_dates_vals, mydb, cursor, online):
    if online:
        mydb = mysql.connector.connect(
                        username = "wod2dh1e3jfuxs210ykt",
                        host = "aws-eu-west-2.connect.psdb.cloud",
                        password = "pscale_pw_zAx3LdXNX0R0YVevbMphKOEjXcSVMc1BKe5PfaCDDB2",
                        database = "moxie_live"
                        )
        cursor = mydb.cursor(buffered=True)
        
    sql = f"INSERT IGNORE INTO {iter_val}_{sensor_id} (DATE_OF_RECORD, VALUE) VALUES (%s, %s)"
    cursor.executemany(sql, formatted_dates_vals)
    mydb.commit()