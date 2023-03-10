import numpy as np
import datetime as dt
from utils.most_expensive.getWholesaleEnergyPrice import get_wholesale_energy_price
from database import open_connection, close_connection


def get_expensive_sensors_and_systems():
    mydb = open_connection()
    cursor = mydb.cursor()

    cursor.execute("SELECT system_id FROM SYSTEMS")
    all_systems = cursor.fetchall()
    price_data = None
    max_sensors = []
    max_systems = []
    for system in all_systems:
        cursor.execute("SELECT sensor_id FROM SENSORS_FOR_{}".format(system[0]))
        all_sensors = cursor.fetchall()

        total_for_system = 0

        for sensor in all_sensors:
            sensor_cost = 0

            cursor.execute(
                "SELECT * FROM READINGS_FOR_{} WHERE READING_DATE >='{}'".format(
                    sensor[0], dt.datetime.strftime(dt.datetime.now() - dt.timedelta(days=4), "%Y-%m-%d")
                )
            )
            response = cursor.fetchall()
            response_length = len(response) // 96
            response = response[: 96 * response_length]

            formatted_timestamps = np.array([dt.datetime.combine(item[0], item[1]) for item in response])
            formatted_timestamps = np.reshape(formatted_timestamps, (-1, 96))

            formatted_values = np.array([float(item[2]) for item in response])
            formatted_values = np.reshape(formatted_values, (-1, 96))

            oldest_date_formatted = dt.datetime.strftime(formatted_timestamps[0, 0], "%d-%m-%Y")
            most_recent_date_formatted = dt.datetime.strftime(
                formatted_timestamps[-1, -1] + dt.timedelta(days=1), "%d-%m-%Y"
            )
            if price_data is None:
                price_data = get_wholesale_energy_price(oldest_date_formatted, most_recent_date_formatted)

            sensor_cost = np.sum(formatted_values * price_data[:, :, 1])
            total_for_system += sensor_cost
            max_sensors.append((sensor[0], sensor_cost))
        max_systems.append((system[0], total_for_system))

    sensors_sorted_by_cost = sorted(max_sensors, key=lambda x: x[1], reverse=True)
    top_3_sensors = sensors_sorted_by_cost[:3]

    systems_sorted_by_cost = sorted(max_systems, key=lambda x: x[1], reverse=True)
    top_3_systems = systems_sorted_by_cost[:3]

    cursor.close()
    close_connection(mydb)
    return {"systems": top_3_systems, "sensors": top_3_sensors}
