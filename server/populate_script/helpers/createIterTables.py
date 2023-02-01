import mysql.connector
def createIterTables(sensor_id, mydb, cursor, online):
    if online:
        mydb = mysql.connector.connect(
                        username = "wod2dh1e3jfuxs210ykt",
                        host = "aws-eu-west-2.connect.psdb.cloud",
                        password = "pscale_pw_zAx3LdXNX0R0YVevbMphKOEjXcSVMc1BKe5PfaCDDB2",
                        database = "moxie_live"
                        )
        cursor = mydb.cursor(buffered=True)
    iter_vals = ["ITER_1", "ITER_2", "ITER_3", "ITER_4"]

    for iter_val in iter_vals:
        sql =f'''CREATE TABLE {iter_val}_{sensor_id}(
                  DATE_OF_RECORD DATETIME NOT NULL PRIMARY KEY,
                  VALUE DECIMAL(15,6) NOT NULL
                  )'''
        cursor.execute(sql)
    mydb.commit()