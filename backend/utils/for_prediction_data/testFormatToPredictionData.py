from .formatToPredictionData import format_to_prediction_data


def test_format_to_prediction_data():
    data_in = [
        ("timestamp_1", 11),
        ("timestamp_2", 12),
        ("timestamp_3", 13),
        ("timestamp_4", 14),
        ("timestamp_5", 15),
        ("timestamp_6", 16),
    ]

    expected_out = [11, 12, 13, 14, 15, 16]

    actual_out = format_to_prediction_data(data_in)

    assert actual_out == expected_out

    print("passed")
