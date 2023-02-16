from typing import List


def format_to_prediction_data(response) -> List[List]:
    formatted_data = [item[1] for item in response]
    return formatted_data
