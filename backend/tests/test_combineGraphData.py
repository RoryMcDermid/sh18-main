import unittest
import numpy as np
from ..utils.extract_features.combineGraphData import combineGraphData

class TestCombineGraphData(unittest.TestCase):

    def test_combineGraphData(self):
        averageData = np.array([1, 2, 3, 4] * 24)
        predictedData = np.array([2, 3, 4, 5] * 24)
        cost = np.array([10, 20, 30, 40] * 24)
        expected_output = np.array([0, 2, 4, 8] * 24)
        self.assertTrue(np.array_equal(combineGraphData(averageData, predictedData, cost), expected_output))

        averageData = np.array([5] * 96)
        predictedData = np.array([10] * 96)
        cost = np.array([20] * 96)
        expected_output = np.array([50] * 96)
        self.assertTrue(np.array_equal(combineGraphData(averageData, predictedData, cost), expected_output))

if __name__ == '__main__':
    unittest.main()





