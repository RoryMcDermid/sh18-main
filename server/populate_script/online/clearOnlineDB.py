import mysql.connector

mydb = mysql.connector.connect(
  database = "moxie_live",
 username = "wod2dh1e3jfuxs210ykt",
  host = "aws-eu-west-2.connect.psdb.cloud",
  password = "pscale_pw_zAx3LdXNX0R0YVevbMphKOEjXcSVMc1BKe5PfaCDDB2"
)


cursor = mydb.cursor()

cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()
sql = ""
for val in tables:
    if val[0] != "SYSTEMS":
        sql += val[0] + ","
    else:
        sql += val[0]

cursor.execute("DROP TABLE " + sql +";")
mydb.commit()