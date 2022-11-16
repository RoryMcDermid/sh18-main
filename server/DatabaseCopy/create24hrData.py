import mysql.connector
from Get24hrData import *
import datetime

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "password",
  database = "moxie_energy"
)

cursor = mydb.cursor()

date = (datetime.datetime.today() - datetime.timedelta(days=1))
formatted_date = str(date.day) + "_" + str(date.month) + "_" + str(date.year)

#date = date.strftime('%Y-%m-%d %H:%M:%S')

sensor_id = input("Which sensor would you like yesterday's 24hr data for?")
system_id = input("What system does this belong to?")

cursor.execute(f"DROP TABLE IF EXISTS 24HR_{sensor_id}_{formatted_date}")

sql =f'''CREATE TABLE 24HR_{sensor_id}_{formatted_date}(
   DATE_OF_RECORD DATETIME NOT NULL PRIMARY KEY,
   SENSOR_ID VARCHAR(15) NOT NULL,
   00_00 DECIMAL(9,6) NOT NULL,
00_15 DECIMAL(9,6) NOT NULL,
00_30 DECIMAL(9,6) NOT NULL,
00_45 DECIMAL(9,6) NOT NULL,
01_00 DECIMAL(9,6) NOT NULL,
01_15 DECIMAL(9,6) NOT NULL,
01_30 DECIMAL(9,6) NOT NULL,
01_45 DECIMAL(9,6) NOT NULL,
02_00 DECIMAL(9,6) NOT NULL,
02_15 DECIMAL(9,6) NOT NULL,
02_30 DECIMAL(9,6) NOT NULL,
02_45 DECIMAL(9,6) NOT NULL,
03_00 DECIMAL(9,6) NOT NULL,
03_15 DECIMAL(9,6) NOT NULL,
03_30 DECIMAL(9,6) NOT NULL,
03_45 DECIMAL(9,6) NOT NULL,
04_00 DECIMAL(9,6) NOT NULL,
04_15 DECIMAL(9,6) NOT NULL,
04_30 DECIMAL(9,6) NOT NULL,
04_45 DECIMAL(9,6) NOT NULL,
05_00 DECIMAL(9,6) NOT NULL,
05_15 DECIMAL(9,6) NOT NULL,
05_30 DECIMAL(9,6) NOT NULL,
05_45 DECIMAL(9,6) NOT NULL,
06_00 DECIMAL(9,6) NOT NULL,
06_15 DECIMAL(9,6) NOT NULL,
06_30 DECIMAL(9,6) NOT NULL,
06_45 DECIMAL(9,6) NOT NULL,
07_00 DECIMAL(9,6) NOT NULL,
07_15 DECIMAL(9,6) NOT NULL,
07_30 DECIMAL(9,6) NOT NULL,
07_45 DECIMAL(9,6) NOT NULL,
08_00 DECIMAL(9,6) NOT NULL,
08_15 DECIMAL(9,6) NOT NULL,
08_30 DECIMAL(9,6) NOT NULL,
08_45 DECIMAL(9,6) NOT NULL,
09_00 DECIMAL(9,6) NOT NULL,
09_15 DECIMAL(9,6) NOT NULL,
09_30 DECIMAL(9,6) NOT NULL,
09_45 DECIMAL(9,6) NOT NULL,
10_00 DECIMAL(9,6) NOT NULL,
10_15 DECIMAL(9,6) NOT NULL,
10_30 DECIMAL(9,6) NOT NULL,
10_45 DECIMAL(9,6) NOT NULL,
11_00 DECIMAL(9,6) NOT NULL,
11_15 DECIMAL(9,6) NOT NULL,
11_30 DECIMAL(9,6) NOT NULL,
11_45 DECIMAL(9,6) NOT NULL,
12_00 DECIMAL(9,6) NOT NULL,
12_15 DECIMAL(9,6) NOT NULL,
12_30 DECIMAL(9,6) NOT NULL,
12_45 DECIMAL(9,6) NOT NULL,
13_00 DECIMAL(9,6) NOT NULL,
13_15 DECIMAL(9,6) NOT NULL,
13_30 DECIMAL(9,6) NOT NULL,
13_45 DECIMAL(9,6) NOT NULL,
14_00 DECIMAL(9,6) NOT NULL,
14_15 DECIMAL(9,6) NOT NULL,
14_30 DECIMAL(9,6) NOT NULL,
14_45 DECIMAL(9,6) NOT NULL,
15_00 DECIMAL(9,6) NOT NULL,
15_15 DECIMAL(9,6) NOT NULL,
15_30 DECIMAL(9,6) NOT NULL,
15_45 DECIMAL(9,6) NOT NULL,
16_00 DECIMAL(9,6) NOT NULL,
16_15 DECIMAL(9,6) NOT NULL,
16_30 DECIMAL(9,6) NOT NULL,
16_45 DECIMAL(9,6) NOT NULL,
17_00 DECIMAL(9,6) NOT NULL,
17_15 DECIMAL(9,6) NOT NULL,
17_30 DECIMAL(9,6) NOT NULL,
17_45 DECIMAL(9,6) NOT NULL,
18_00 DECIMAL(9,6) NOT NULL,
18_15 DECIMAL(9,6) NOT NULL,
18_30 DECIMAL(9,6) NOT NULL,
18_45 DECIMAL(9,6) NOT NULL,
19_00 DECIMAL(9,6) NOT NULL,
19_15 DECIMAL(9,6) NOT NULL,
19_30 DECIMAL(9,6) NOT NULL,
19_45 DECIMAL(9,6) NOT NULL,
20_00 DECIMAL(9,6) NOT NULL,
20_15 DECIMAL(9,6) NOT NULL,
20_30 DECIMAL(9,6) NOT NULL,
20_45 DECIMAL(9,6) NOT NULL,
21_00 DECIMAL(9,6) NOT NULL,
21_15 DECIMAL(9,6) NOT NULL,
21_30 DECIMAL(9,6) NOT NULL,
21_45 DECIMAL(9,6) NOT NULL,
22_00 DECIMAL(9,6) NOT NULL,
22_15 DECIMAL(9,6) NOT NULL,
22_30 DECIMAL(9,6) NOT NULL,
22_45 DECIMAL(9,6) NOT NULL,
23_00 DECIMAL(9,6) NOT NULL,
23_15 DECIMAL(9,6) NOT NULL,
23_30 DECIMAL(9,6) NOT NULL,
23_45 DECIMAL(9,6) NOT NULL
)'''



cursor.execute(sql)

sql = f'''ALTER TABLE 24HR_{sensor_id}_{formatted_date} 
        ADD FOREIGN KEY (SENSOR_ID) REFERENCES SENSORS_FOR_{system_id}(SENSOR_ID);
'''
cursor.execute(sql)


data24hr = get24hrData(sensor_id, system_id)

##up to reading the file in correctly, now just have to parse it and get it into DB!

parsed_24hr_data = []

for data in data24hr["systems"][0]["sensors"][0]["data"]:
  parsed_24hr_data.append(list(data["values"].values())[0])

parsed_24hr_data = tuple(x for x in parsed_24hr_data)
data_as_string = ",".join(str(parsed_24hr_data))
percent_s = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"

sql = f"INSERT INTO 24HR_{sensor_id}_{formatted_date} (DATE_OF_RECORD, SENSOR_ID, 00_00, 00_15,00_30,00_45,01_00,01_15,01_30,01_45,02_00,02_15,02_30,02_45,03_00,03_15,03_30,03_45,04_00,04_15,04_30,04_45,05_00,05_15,05_30,05_45,06_00,06_15,06_30,06_45,07_00,07_15,07_30,07_45,08_00,08_15,08_30,08_45,09_00,09_15,09_30,09_45,10_00,10_15,10_30,10_45,11_00,11_15,11_30,11_45,12_00,12_15,12_30,12_45,13_00,13_15,13_30,13_45,14_00,14_15,14_30,14_45,15_00,15_15,15_30,15_45,16_00,16_15,16_30,16_45,17_00,17_15,17_30,17_45,18_00,18_15,18_30,18_45,19_00,19_15,19_30,19_45,20_00,20_15,20_30,20_45,21_00,21_15,21_30,21_45,22_00,22_15,22_30,22_45,23_00,23_15,23_30,23_45) VALUES ({percent_s})"
vals = (date.strftime('%Y-%m-%d'), sensor_id) + parsed_24hr_data
cursor.execute(sql, vals)
mydb.commit()

