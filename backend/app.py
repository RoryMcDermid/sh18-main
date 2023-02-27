from utils.data_formatting.formatToChartData import format_to_chart_data
from database import open_connection, close_connection
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

# ----------- ENDPOINTS


@app.get("/systems", response_description="Get list of all systems")
async def get_systems():
    mydb = open_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM SYSTEMS")
    systems = cursor.fetchall()
    cursor.close()
    close_connection(mydb)
    return systems


@app.get("/systems/{systemid}/sensors", response_description="Get list of all sensors in a system")
async def get_sensors(systemid):
    mydb = open_connection()
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM SENSORS_FOR_{systemid}")
    sensors = cursor.fetchall()
    cursor.close()
    close_connection(mydb)
    return sensors


@app.get(
    "/sensors/{sensorids}/chartformat",
    response_description="Get reading data for multiple sensors based on startdate and enddate",
)
async def get_sensor_readings(sensorids, startDate, endDate):
    mydb = open_connection()
    result = []
    if "," in sensorids:
        for sensorid in sensorids.split(","):
            print(sensorid)
            cursor = mydb.cursor()
            cursor.execute(
                f"SELECT * FROM READINGS_FOR_{sensorid} WHERE READING_DATE>='{startDate}' AND READING_DATE<'{endDate}'"
            )
            result.append(cursor.fetchall())
            cursor.close()
    else:
        cursor = mydb.cursor()
        cursor.execute(
            f"SELECT * FROM READINGS_FOR_{sensorids} WHERE READING_DATE>='{startDate}' AND READING_DATE<'{endDate}'"
        )
        result.append(cursor.fetchall())
        cursor.close()

    close_connection(mydb)
    return result


@app.get("/sensors/{sensorid}", response_description="Get ALL reading data for ONE sensor")
async def get_sensor_readings(sensorid):
    mydb = open_connection()
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM READINGS_FOR_{sensorid}")
    readings = cursor.fetchall()
    cursor.close()
    close_connection(mydb)
    return readings
