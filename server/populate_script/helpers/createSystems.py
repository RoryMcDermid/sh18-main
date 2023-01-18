import mysql.connector
from helpers.getSystemsList import *


def create_systems(mydb, cursor):

  cursor.execute("DROP TABLE IF EXISTS SYSTEMS")

  sql ='''CREATE TABLE SYSTEMS(
    SYSTEM_ID INT NOT NULL PRIMARY KEY,
    SYSTEM_NAME VARCHAR(150) NOT NULL,
  )'''
  cursor.execute(sql)

  systems_list = getSystemsList()

  system_ids = []

  for (system_id, system_info) in systems_list.items():
      system_ids.append(system_id)
      sql = "INSERT INTO SYSTEMS (SYSTEM_ID, SYSTEM_NAME) VALUES (%s, %s)"
      vals = (system_id, system_info["name"])
      cursor.execute(sql, vals)
      mydb.commit()


  return system_ids