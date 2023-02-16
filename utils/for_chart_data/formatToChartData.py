from typing import List


def format_to_chart_data(response: List[List[dict]]) -> List[List]:
    formatted_data = []

    for rows in zip(*response):
        timestamp = rows[0]["DATE_OF_RECORD"]
        values = [item["VALUE"] for item in rows]
        formatted_data.append([timestamp, *values])

    return formatted_data
