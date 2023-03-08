import numpy as np
import datetime as dt
from fastapi import APIRouter
from utils.most_expensive.getMidnight import get_midnight
from utils.extract_features.combineGraphData import combine_graph_data
from utils.extract_features.generateSuggestions import generate_suggestions
from utils.extract_features.getPointOfInterest import get_points_of_interest
from utils.database_fetches.get_all_readings_for_sensors import get_all_readings_for_sensor
from utils.database_fetches.get_readings_for_sensors import get_readings_for_sensors
from utils.data_formatting.formatForCompareScreen import format_for_compare_screen
from utils.data_formatting.formatToPredictionData import format_to_prediction_data
from utils.get_features.averageFromGroup import get_average_from_group
from utils.prediction.predictEnergyUsage import predict_EnergyUsage
from utils.get_features.generateMockData import generate_mock_data
from utils.data_formatting.formatForForecastScreen import format_for_forecast_screen
from utils.most_expensive.getWholesaleEnergyPrice import get_wholesale_energy_price


router = APIRouter()


@router.get(
    "/{sensorids}/compare-and-display",
    response_description="Get reading data for multiple sensors based on startdate and enddate",
)
async def get_sensor_readings(sensorids, startDate, endDate):
    readings = get_readings_for_sensors(sensorids.split(","), startDate, endDate)
    return format_for_compare_screen(readings)


@router.get("/{sensorid}/forecast", response_description="Get prediction data for ONE sensor")
async def get_forcast_data(sensorid):
    reading_data = generate_mock_data(get_all_readings_for_sensor(sensorid))
    prediction = predict_EnergyUsage(format_to_prediction_data(reading_data))
    average = get_average_from_group(reading_data)
    chart_data = format_for_forecast_screen(prediction, average)

    start_string = dt.datetime.strftime(get_midnight(dt.datetime.now()) - dt.timedelta(days=1), "%d-%m-%Y")
    end_string = dt.datetime.strftime(get_midnight(dt.datetime.now()), "%d-%m-%Y")
    cost = get_wholesale_energy_price(start_string, end_string)[0][:, 1]

    points_of_interest = get_points_of_interest(combine_graph_data(prediction, average, cost))
    suggestion_data = generate_suggestions(points_of_interest)
    return {"chartData": chart_data, "suggestionData": suggestion_data}
