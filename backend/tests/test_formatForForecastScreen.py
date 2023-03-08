import unittest
from ..utils.data_formatting.formatForForecastScreen import format_for_forecast_screen


class Test_format_for_forecast_screen(unittest.TestCase):

    def test_format_for_forecast_screen(self):
        prediction = [
            [[10], [20], [30], [40]],
            [[50], [60], [70], [80]],
            [[90], [100], [110], [120]],
        ]
        average = [[25], [65], [105]]
        expected_output = [['00:00', [[10], [20], [30], [40]], [25]],
                           ['00:15', [[50], [60], [70], [80]], [65]],
                           ['00:30', [[90], [100], [110], [120]], [105]]]

        self.assertEqual(format_for_forecast_screen(prediction, average), expected_output)

    def test_format_for_forecast_screen_not_empty(self):
        prediction = [
            [[10], [20], [30], [40]],
            [[50], [60], [70], [80]],
            [[90], [100], [110], [120]],
        ]
        average = [[25], [65], [105]]

        expected_output = []
        self.assertNotEqual(format_for_forecast_screen(prediction, average), expected_output)

    def test_empty(self):
        prediction = []
        average = []
        expected_output = []

        self.assertEqual(format_for_forecast_screen(prediction, average), expected_output)


if __name__ == '__main__':
    unittest.main()