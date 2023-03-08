import unittest
import datetime as dt
from ..utils.data_formatting.formatToChartData2 import format_to_chart_data2


class TestFormatToChartData2(unittest.TestCase):

    def test_format_to_chart_data2(self):
        prediction = [
            [[10], [20], [30], [40]],
            [[50], [60], [70], [80]],
            [[90], [100], [110], [120]],
        ]
        average = [[25], [65], [105]]

        today = dt.date.today()
        midnight_today = dt.datetime.combine(today, dt.datetime.min.time())
        expected_output = [
            [dt.datetime.strftime(midnight_today, "%Y-%m-%dT%H:%M:%S"), [[10], [20], [30], [40]], [25]],
            [dt.datetime.strftime(midnight_today + dt.timedelta(minutes=15), "%Y-%m-%dT%H:%M:%S"),
             [[50], [60], [70], [80]], [65]],
            [dt.datetime.strftime(midnight_today + dt.timedelta(minutes=30), "%Y-%m-%dT%H:%M:%S"),
             [[90], [100], [110], [120]], [105]],
        ]

        self.assertEqual(format_to_chart_data2(prediction, average), expected_output)

    def test_format_to_chart_data2_not_empty(self):
        prediction = [
            [[10], [20], [30], [40]],
            [[50], [60], [70], [80]],
            [[90], [100], [110], [120]],
        ]
        average = [[25], [65], [105]]

        expected_output = []
        self.assertNotEqual(format_to_chart_data2(prediction, average), expected_output)

    def test_empty(self):
        prediction = []
        average = []
        expected_output = []

        self.assertEqual(format_to_chart_data2(prediction, average), expected_output)


if __name__ == '__main__':
    unittest.main()