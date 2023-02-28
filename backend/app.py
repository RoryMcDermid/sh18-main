from utils.data_formatting.formatToChartData import format_to_chart_data
from utils.data_formatting.formatToPredictionData import format_to_prediction_data
from utils.get_features.averageFromGroup import get_average_from_group
from database import open_connection, close_connection
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from utils.prediction.predictEnergyUsage import predict_EnergyUsage
from utils.get_features.generateMockData import generate_mock_data

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
    "/sensors/{sensorids}/compareanddisplay",
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
    return format_to_chart_data(result)


# @app.get("/sensors/{sensorid}", response_description="Get ALL reading data for ONE sensor")
# async def get_sensor_readings(sensorid):
#     mydb = open_connection()
#     cursor = mydb.cursor()
#     cursor.execute(f"SELECT * FROM READINGS_FOR_{sensorid}")
#     readings = cursor.fetchall()
#     cursor.close()
#     close_connection(mydb)
#     return readings


@app.get("/sensors/{sensorid}/predict", response_description="Get prediction data for ONE sensor")
async def get_sensor_readings(sensorid):
    mydb = open_connection()
    cursor = mydb.cursor()
    cursor.execute(f"SELECT * FROM READINGS_FOR_{sensorid}")
    readings = cursor.fetchall()
    cursor.close()
    close_connection(mydb)

    mockdata = generate_mock_data(readings)
    prediction = predict_EnergyUsage(format_to_prediction_data(mockdata))
    average = get_average_from_group(mockdata)

    return {"prediction": prediction, "average": average}
