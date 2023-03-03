from typing import List
import datetime as dt


def format_to_chart_data2(prediction: List[List[List]], average) -> List[List]:
    formatted_data = []
    today = dt.date.today()
    midnight_today = dt.datetime.combine(today, dt.datetime.min.time())

    for i, vals in enumerate(zip(prediction, average)):
        timestamp = dt.datetime.strftime(
            midnight_today + dt.timedelta(minutes=15*i), "%Y-%m-%dT%H:%M:%S")
        formatted_data.append([timestamp, *vals])

    return formatted_data
