from typing import List
import numpy as np


def format_for_expense_analysing(response) -> List[List]:
    formatted_timestamps = np.array([item[0] for item in response])
    formatted_timestamps = np.reshape(formatted_timestamps, (-1, 96))

    formatted_values = np.array([item[1] for item in response])
    formatted_values = np.reshape(formatted_values, (-1, 96))

    return np.column_stack((formatted_values, formatted_values))
