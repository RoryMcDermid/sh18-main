import psycopg2
import datetime as dt


connection_string = "postgresql://moxie:iYmwQU_OL2HI1-fiiOqSuQ@fooled-dolphin-7094.8nj.cockroachlabs.cloud:26257/moxie_data?sslmode=verify-full"
conn = psycopg2.connect(connection_string)
cursor = conn.cursor()

cursor.execute(f"SELECT * FROM READINGS_FOR_6311171 ORDER BY (READING_DATE) DESC")
print(cursor.fetchone())
cursor.close()
conn.close()