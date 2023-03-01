from typing import List
import datetime as dt


"""
[
    [
        [timestamp_1, value_1], 
        [timestamp_2, value_2]
    ],
    [
        [timestamp_1, value_1b], 
        [timestamp_2, value_2b]
    ]
]
"""


def format_to_chart_data(response: List[List[List]]) -> List[List]:
    formatted_data = []

    for rows in zip(*response):
        timestamp = dt.datetime.combine(rows[0][0], rows[0][1])
        values = [item[2] for item in rows]
        formatted_data.append([timestamp, *values])

    return formatted_data
