from typing import List
import numpy as np


def format_for_expense_analysing(response) -> List[List]:
    response_length = len(response) // 96
    response = response[: 96 * response_length]

    formatted_timestamps = np.array([item[0] for item in response])
    formatted_timestamps = np.reshape(formatted_timestamps, (-1, 96))

    formatted_values = np.array([item[1] for item in response])
    formatted_values = np.reshape(formatted_values, (-1, 96))

    stack = np.dstack((formatted_timestamps, formatted_values))
    return stack.tolist()
