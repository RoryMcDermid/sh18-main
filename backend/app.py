from utils.most_expensive.getWholesaleEnergyPrice import *
from utils.data_formatting.formatToChartData import format_to_chart_data
from utils.data_formatting.formatToPredictionData import format_to_prediction_data
from utils.get_features.averageFromGroup import get_average_from_group
from database import open_connection, close_connection
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import numpy as np
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
    "/sensors/{sensorids}/compare-and-display",
    response_description="Get reading data for multiple sensors based on startdate and enddate",
)
async def get_sensor_readings(sensorids, startDate, endDate):
    mydb = open_connection()
    result = []
    cursor = mydb.cursor()

    if "," in sensorids:
        for sensorid in sensorids.split(","):
            print(sensorid)

            cursor.execute(
                f"SELECT * FROM READINGS_FOR_{sensorid} WHERE READING_DATE>='{startDate}' AND READING_DATE<'{endDate}'"
            )
            result.append(cursor.fetchall())

    else:
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


@app.get("/sensors/{sensorid}/forcast", response_description="Get prediction data for ONE sensor")
async def get_forcast_data(sensorid):
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


@app.get(
    "/expensive-systems-sensors",
    response_description="Returns the top 3 most expensive systems or sensors. Returned format is a list of tuples, containing the ID along with total cost. E.g. [(1234, 1000.45242), (2791, 923.59532), (3399, 721.80021)]",
)
async def get_expensive_sensors_systems():
    mydb = open_connection()
    cursor = mydb.cursor()

    cursor.execute("SELECT system_id FROM SYSTEMS")
    all_systems = cursor.fetchall()
    price_data = None
    max_sensors = []
    max_systems = []
    for system in all_systems:
        cursor.execute(
            "SELECT sensor_id FROM SENSORS_FOR_{}".format(system[0]))
        all_sensors = cursor.fetchall()

        total_for_system = 0

        for sensor in all_sensors:
            sensor_cost = 0

            cursor.execute("SELECT * FROM READINGS_FOR_{} WHERE READING_DATE >='{}'".format(
                sensor[0], dt.datetime.strftime(dt.datetime.now() - dt.timedelta(days=4), "%Y-%m-%d")))
            response = cursor.fetchall()
            response_length = len(response) // 96
            response = response[: 96 * response_length]

            formatted_timestamps = np.array(
                [dt.datetime.combine(item[0], item[1]) for item in response])
            formatted_timestamps = np.reshape(formatted_timestamps, (-1, 96))

            formatted_values = np.array([float(item[2]) for item in response])
            formatted_values = np.reshape(formatted_values, (-1, 96))

            oldest_date_formatted = dt.datetime.strftime(
                formatted_timestamps[0, 0], "%d-%m-%Y")
            most_recent_date_formatted = dt.datetime.strftime(
                formatted_timestamps[-1, -1] + dt.timedelta(days=1), "%d-%m-%Y")
            if price_data is None:
                price_data = getWholesaleEnergyPrice(
                    oldest_date_formatted, most_recent_date_formatted)

            sensor_cost = np.sum(formatted_values * price_data[:, :, 1])
            total_for_system += sensor_cost
            max_sensors.append((sensor[0], sensor_cost))
        max_systems.append((system[0], total_for_system))

    sensors_sorted_by_cost = sorted(
        max_sensors, key=lambda x: x[1], reverse=True)
    top_3_sensors = sensors_sorted_by_cost[:3]

    systems_sorted_by_cost = sorted(
        max_systems, key=lambda x: x[1], reverse=True)
    top_3_systems = systems_sorted_by_cost[:3]

    cursor.close()
    close_connection(mydb)
    return {"systems": top_3_systems, "sensors": top_3_sensors}
