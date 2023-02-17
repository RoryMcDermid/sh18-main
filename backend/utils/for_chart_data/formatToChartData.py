from typing import List


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
        timestamp = rows[0][0]
        values = [item[1] for item in rows]
        formatted_data.append([timestamp, *values])

    return formatted_data
