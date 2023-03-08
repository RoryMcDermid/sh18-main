from datetime import datetime
import unittest
from ..utils.get_features.generateMockData import *


class TestGetDateBoundaries(unittest.TestCase):
    def test_get_date_boundaries(self):
        data = [
            [datetime(2022, 1, 1).date(), datetime(2022, 1, 1, 0, 0, 0).time()],
            [datetime(2022, 1, 1).date(), datetime(2022, 1, 1, 0, 15, 0).time()],
            [datetime(2022, 1, 2).date(), datetime(2022, 1, 2, 0, 0, 0).time()],
            [datetime(2022, 1, 2).date(), datetime(2022, 1, 2, 0, 15, 0).time()],
            [datetime(2022, 1, 3).date(), datetime(2022, 1, 3, 0, 0, 0).time()]
        ]
        start_date, end_date = get_date_boundaries(data)
        self.assertEqual(start_date, datetime(2022, 1, 1, 0, 0, 0))
        self.assertEqual(end_date, datetime(2022, 1, 3, 0, 0, 0))

if __name__ == '__main__':
    unittest.main()
