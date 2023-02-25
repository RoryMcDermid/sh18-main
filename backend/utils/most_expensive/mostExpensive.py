import requests
from getWholesaleEnergyPrice import *

# Function for returning the top 3 most expensive systems or sensors, depending on 
# boolean value given. Returned format is a list of tuples, containing the ID along with
# total cost. E.g. [(1234, 1000.45242), (2791, 923.59532), (3399, 721.80021)]
def mostExpensiveData(wanting_system):

    # Set up the API endpoint URL
    base_url = "http://127.0.0.1:5000/"

    # Send the HTTP request and handle the response
    all_systems = requests.get(base_url + "systems").json()

    all_systems = [[2417,"aaaa"]]
    price_data = None
    max_sensors = []
    max_systems = []
    for system in all_systems:
        all_sensors = requests.get(base_url + f"systems/{ system[0]}/sensors").json()
        total_for_system = 0

        for sensor in all_sensors:
            sensor_cost = 0
            api_request = requests.get(base_url + f"sensors/evaluation/{sensor[0]}")
            response = api_request.json()
            response_length = len(response) // 96
            response = response[: 96 * response_length]

            formatted_timestamps = np.array([item[0] for item in response])
            formatted_timestamps = np.reshape(formatted_timestamps, (-1, 96))

            formatted_values = np.array([float(item[1]) for item in response])
            formatted_values = np.reshape(formatted_values, (-1, 96))

            oldest_date_formatted = dt.datetime.strftime(dt.datetime.strptime(formatted_timestamps[0,0], "%Y-%m-%dT%H:%M:%S"), "%d-%m-%Y")
            most_recent_date_formatted = dt.datetime.strftime(dt.datetime.strptime(formatted_timestamps[-1,-1], "%Y-%m-%dT%H:%M:%S"), "%d-%m-%Y")
            if price_data is None:
                price_data = getWholesaleEnergyPrice(oldest_date_formatted, most_recent_date_formatted)

            sensor_cost = np.sum(formatted_values * price_data[:,:,1])
            total_for_system += sensor_cost
            max_sensors.append((sensor[0], sensor_cost))
        max_systems.append((system[0], total_for_system))

    sensors_sorted_by_cost = sorted(max_sensors, key=lambda x: x[1], reverse=True)
    top_3_sensors = sensors_sorted_by_cost[:3]

    systems_sorted_by_cost = sorted(max_systems, key=lambda x: x[1], reverse=True)
    top_3_systems = systems_sorted_by_cost[:3]

    if wanting_system:
        return top_3_systems
    else: 
        return top_3_sensors