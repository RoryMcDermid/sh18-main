from formatToChartData import format_to_chart_data


def test():
    data_in = [
        [
            {"DATE_OF_RECORD": "timestamp_1", "VALUE": 111},
            {"DATE_OF_RECORD": "timestamp_2", "VALUE": 222},
            {"DATE_OF_RECORD": "timestamp_3", "VALUE": 333},
        ],
        [
            {"DATE_OF_RECORD": "timestamp_1", "VALUE": 110},
            {"DATE_OF_RECORD": "timestamp_2", "VALUE": 220},
            {"DATE_OF_RECORD": "timestamp_3", "VALUE": 330},
        ],
        [
            {"DATE_OF_RECORD": "timestamp_1", "VALUE": 101},
            {"DATE_OF_RECORD": "timestamp_2", "VALUE": 202},
            {"DATE_OF_RECORD": "timestamp_3", "VALUE": 303},
        ],
    ]

    expected_out = [["timestamp_1", 111, 110, 101], ["timestamp_2", 222, 220, 202], ["timestamp_3", 333, 330, 303]]

    actual_out = format_to_chart_data(data_in)

    assert actual_out == expected_out


test()
