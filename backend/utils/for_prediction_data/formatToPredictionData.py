from typing import List
import numpy as np


def format_to_prediction_data(response) -> List[List]:
    formatted_data = np.array([item[1] for item in response])
    return np.reshape(formatted_data, (-1, 96))
