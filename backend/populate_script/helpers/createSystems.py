import mysql.connector
from helpers.getSystemsList import *
import os
import dotenv

def create_systems(mydb, cursor, mock=0, online = False):

  if online:
    env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    dotenv.load_dotenv(dotenv_path=env_path)

    mydb = mysql.connector.connect(
                        username=os.environ.get('DB_USERNAME'),
                        host=os.environ.get('DB_HOST'),
                        password=os.environ.get('DB_PASSWORD'),
                        database=os.environ.get('DB')
                    )
    cursor = mydb.cursor(buffered=True)

  cursor.execute("DROP TABLE IF EXISTS SYSTEMS")
  sql ='''CREATE TABLE SYSTEMS (SYSTEM_ID INT NOT NULL PRIMARY KEY, SYSTEM_NAME VARCHAR(150) NOT NULL)'''
  cursor.execute(sql)

  if mock == 0:
    systems_dict = getSystemsList()
  else:
    systems_dict = mock
     
  system_ids = []
  vals = []
  for (system_id, system_info) in systems_dict.items():
    system_ids.append(int(system_id))
    vals.append((system_id, system_info["name"]))
  sql = "INSERT INTO SYSTEMS (SYSTEM_ID, SYSTEM_NAME) VALUES (%s, %s)"

  if online:
    env_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    dotenv.load_dotenv(dotenv_path=env_path)

    mydb = mysql.connector.connect(
                        username=os.environ.get('DB_USERNAME'),
                        host=os.environ.get('DB_HOST'),
                        password=os.environ.get('DB_PASSWORD'),
                        database=os.environ.get('DB')
                    )
    cursor = mydb.cursor(buffered=True)
      
  cursor.executemany(sql, vals)
  mydb.commit()

  return system_ids