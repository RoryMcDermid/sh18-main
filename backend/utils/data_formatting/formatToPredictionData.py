from typing import List
import numpy as np


def format_to_prediction_data(response) -> List[List]:
    formatted_data = np.array([item[1] for item in response])
    if len(formatted_data) % 96 != 0:
        remainder = len(formatted_data) % 96
        formatted_data = formatted_data[0:-remainder]
    return np.reshape(formatted_data, (-1, 96))
