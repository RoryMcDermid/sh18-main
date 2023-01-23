def addToIter(sensor_id, iter_val, formatted_dates_vals, mydb, cursor):
    sql = f"INSERT IGNORE INTO {iter_val}_{sensor_id} (DATE_OF_RECORD, VALUE) VALUES (%s, %s)"
    cursor.executemany(sql, formatted_dates_vals)
    mydb.commit()