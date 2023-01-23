def dropIterTables(sensor_id, mydb, cursor):
    iter_vals = ["ITER_1", "ITER_2", "ITER_3", "ITER_4"]

    for iter_val in iter_vals:
        sql =f'''DROP TABLE {iter_val}_{sensor_id}'''
        cursor.execute(sql)
    mydb.commit()