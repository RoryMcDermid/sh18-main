from database import open_connection, close_connection
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

# ----------- ENDPOINTS


@app.get("/systems", response_description="Get list of all systems")
async def get_systems():
    mydb = open_connection()
    cursor = mydb.cursor(buffered=True)
    cursor.execute("SELECT * FROM SYSTEMS")
    systems = cursor.fetchall()
    cursor.close()
    close_connection(mydb)
    return systems


@app.get("/systems/{systemid}/sensors", response_description="Get list of all sensors in a system")
async def get_sensors(systemid):
    mydb = open_connection()
    cursor = mydb.cursor(buffered=True)
    cursor.execute("SELECT * FROM SENSORS_FOR_{}".format(systemid))
    sensors = cursor.fetchall()
    cursor.close()
    close_connection(mydb)
    return sensors


@app.get("/sensors/compare/{sensorids}", response_description="Get reading data for multiple sensors based on startdate and enddate")
async def get_sensor_readings(sensorids, startDate, endDate):
    mydb = open_connection()
    result = []
    if "," in sensorids:
        for sensorid in sensorids.split(","):
            print(sensorid)
            cursor = mydb.cursor(buffered=True)
            cursor.execute(
                "SELECT * FROM READINGS_FOR_{} WHERE READING_DATE>='{}' AND READING_DATE<'{}'".format(sensorid, startDate, endDate))
            result.append(cursor.fetchall())
            cursor.close()
    else:
        cursor = mydb.cursor(buffered=True)
        cursor.execute(
            "SELECT * FROM READINGS_FOR_{} WHERE READING_DATE>='{}' AND READING_DATE<'{}'".format(sensorids, startDate, endDate))
        result.append(cursor.fetchall())
        cursor.close()

    close_connection(mydb)
    return result


@app.get("/sensors/forcast/{sensorid}", response_description="Get ALL reading data for ONE sensor")
async def get_sensor_readings(sensorid):
    mydb = open_connection()
    cursor = mydb.cursor(buffered=True)
    cursor.execute("SELECT * FROM READINGS_FOR_{}".format(sensorid))
    readings = cursor.fetchall()
    cursor.close()
    close_connection(mydb)
    return readings
