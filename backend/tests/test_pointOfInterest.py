import unittest
from ..utils.extract_features.getPointOfInterest import *

class TestMax(unittest.TestCase):

    def test_max(self):
        array = [-3, 0, 2, 3, 1, -1, -2, -1]
        expected = 3
        result = max(array)
        self.assertEqual(result, expected)


class TestMin(unittest.TestCase):

    def test_min(self):
        array = [-3, 0, 2, 3, 1, -1, -2, -1]
        expected = 0
        result = min(array)
        self.assertEqual(result, expected)