import unittest
import datetime as dt
from ..utils.data_formatting.formatForCompareScreen import format_for_compare_screen


class TestFormatToChartData(unittest.TestCase):

    def test_format_to_chart_data(self):
        response = [
            [[dt.date(2022, 1, 1), dt.time(0, 0), 10], [dt.date(2022, 1, 1), dt.time(0, 5), 20]],
            [[dt.date(2022, 1, 1), dt.time(0, 1), 30], [dt.date(2022, 1, 1), dt.time(0, 6), 40]],
            [[dt.date(2022, 1, 1), dt.time(0, 2), 50], [dt.date(2022, 1, 1), dt.time(0, 7), 60]],
            [[dt.date(2022, 1, 1), dt.time(0, 3), 70], [dt.date(2022, 1, 1), dt.time(0, 8), 80]],
            [[dt.date(2022, 2, 2), dt.time(0, 4), 90], [dt.date(2022, 1, 1), dt.time(0, 9), 100]],
        ]

        expected_output = [['01-01 00:00', 10, 30, 50, 70, 90], ['01-01 00:05', 20, 40, 60, 80, 100]]

        self.assertEqual(format_for_compare_screen(response), expected_output)

    def test_format_for_compare_screen_not_empty(self):
        response = [
            [[dt.date(2022, 1, 1), dt.time(0, 0), 10], [dt.date(2022, 1, 1), dt.time(0, 5), 20]],
            [[dt.date(2022, 1, 1), dt.time(0, 1), 30], [dt.date(2022, 1, 1), dt.time(0, 6), 40]],
            [[dt.date(2022, 1, 1), dt.time(0, 2), 50], [dt.date(2022, 1, 1), dt.time(0, 7), 60]],
            [[dt.date(2022, 1, 1), dt.time(0, 3), 70], [dt.date(2022, 1, 1), dt.time(0, 8), 80]],
            [[dt.date(2022, 2, 2), dt.time(0, 4), 90], [dt.date(2022, 1, 1), dt.time(0, 9), 100]],
        ]
        expected_output = []

        self.assertNotEqual(format_for_compare_screen(response), expected_output)

    def test_empty(self):
        response = []
        expected_output = []

        self.assertEqual(format_for_compare_screen(response), expected_output)


if __name__ == '__main__':
    unittest.main()
