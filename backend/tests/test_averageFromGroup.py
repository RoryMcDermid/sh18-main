import unittest
import numpy as np
import datetime as dt
from ..utils.get_features.averageFromGroup import *

class TestGetGroupInfo(unittest.TestCase):
    def test_get_group_info_january_tuesday(self):
        date = dt.date(2023, 1, 3)
        expected = (1, 1)  # First month Tuesday
        result = get_group_info(date)
        self.assertEqual(result, expected)

    def test_get_group_info_february_friday(self):
        date = dt.date(2023, 2, 10)  # Friday in February
        expected = (2, 4)  # Second month Friday
        result = get_group_info(date)
        self.assertEqual(result, expected)

    def test_get_group_info_december_sunday(self):
        date = dt.date(2023, 12, 31)
        expected = (12, 6)
        result = get_group_info(date)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
