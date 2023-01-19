import mysql.connector
from helpers.getSystemsList import *


def create_systems(mydb, cursor):

  cursor.execute("DROP TABLE IF EXISTS SYSTEMS")

  sql ='''CREATE TABLE SYSTEMS (SYSTEM_ID INT NOT NULL PRIMARY KEY, SYSTEM_NAME VARCHAR(150) NOT NULL)'''

  cursor.execute(sql)

  systems_dict = getSystemsList()
     
  system_ids = []
  vals = []

  for (system_id, system_info) in systems_dict.items():
    system_ids.append(system_id)
    vals.append((system_id, system_info["name"]))
  sql = "INSERT INTO SYSTEMS (SYSTEM_ID, SYSTEM_NAME) VALUES (%s, %s)"
      
  cursor.executemany(sql, vals)
  mydb.commit()


  return system_ids