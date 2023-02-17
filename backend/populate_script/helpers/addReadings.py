import mysql.connector
def addReadings(sensor_id, formatted_dates_vals, mydb, cursor, online):
    if online:
        mydb = mysql.connector.connect(
                        username = "wod2dh1e3jfuxs210ykt",
                        host = "aws-eu-west-2.connect.psdb.cloud",
                        password = "pscale_pw_zAx3LdXNX0R0YVevbMphKOEjXcSVMc1BKe5PfaCDDB2",
                        database = "moxie_live"
                        )
        cursor = mydb.cursor(buffered=True)
    sql = f"INSERT IGNORE INTO READINGS_FOR_{sensor_id} (READING_DATE, VALUE) VALUES (%s, %s)"
    cursor.executemany(sql, formatted_dates_vals)
    mydb.commit()