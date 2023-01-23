def createIterTables(sensor_id, mydb, cursor):
    iter_vals = ["ITER_1", "ITER_2", "ITER_3", "ITER_4"]

    for iter_val in iter_vals:
        sql =f'''CREATE TABLE {iter_val}_{sensor_id}(
                  DATE_OF_RECORD DATETIME NOT NULL PRIMARY KEY,
                  VALUE DECIMAL(15,6) NOT NULL
                  )'''
        cursor.execute(sql)
    mydb.commit()