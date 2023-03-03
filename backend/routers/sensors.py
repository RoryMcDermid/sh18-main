import numpy as np
import datetime as dt
from fastapi import APIRouter
from utils.database_fetches.get_all_readings_for_sensors import get_all_readings_for_sensor
from utils.database_fetches.get_readings_for_sensors import get_readings_for_sensors
from utils.data_formatting.formatToChartData import format_to_chart_data
from utils.data_formatting.formatToPredictionData import format_to_prediction_data
from utils.get_features.averageFromGroup import get_average_from_group
from utils.prediction.predictEnergyUsage import predict_EnergyUsage
from utils.get_features.generateMockData import generate_mock_data
from utils.data_formatting.formatToChartData2 import format_to_chart_data2
from utils.most_expensive.getWholesaleEnergyPrice import getWholesaleEnergyPrice

router = APIRouter()


@router.get(
    "/{sensorids}/compare-and-display",
    response_description="Get reading data for multiple sensors based on startdate and enddate",
)
async def get_sensor_readings(sensorids, startDate, endDate):
    readings = get_readings_for_sensors(
        sensorids.split(","), startDate, endDate)
    return format_to_chart_data(readings)


@router.get("/{sensorid}/forecast", response_description="Get prediction data for ONE sensor")
async def get_forcast_data(sensorid):
    reading_data = generate_mock_data(get_all_readings_for_sensor(sensorid))
    prediction = predict_EnergyUsage(format_to_prediction_data(reading_data))
    average = get_average_from_group(reading_data)

    return {"chartData": format_to_chart_data2(prediction, average), "suggestion": []}
