import psycopg2

connection_string = "postgresql://moxie:iYmwQU_OL2HI1-fiiOqSuQ@fooled-dolphin-7094.8nj.cockroachlabs.cloud:26257/moxie_data?sslmode=verify-full"

mydb = psycopg2.connect(connection_string)
cursor = mydb.cursor()
cursor.execute("SHOW TABLES;")
tables = cursor.fetchall()

for val in tables:
    cursor.execute("DROP TABLE " + val[1] +";")
mydb.commit()