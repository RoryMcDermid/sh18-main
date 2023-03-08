from typing import List
import datetime as dt


def format_for_compare_screen(response: List[List[List]]) -> List[List]:
    formatted_data = []

    for rows in zip(*response):
        timestamp = dt.datetime.strftime(dt.datetime.combine(rows[0][0], rows[0][1]), "%d-%m %H:%M")
        values = [item[2] for item in rows]
        formatted_data.append([timestamp, *values])

    return formatted_data
