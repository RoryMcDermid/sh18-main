import unittest
import numpy as np
from ..utils.prediction.predictEnergyUsage import predict_EnergyUsage


class TestPredictEnergyUsage(unittest.TestCase):

    def test_output_shape(self):
        # test shape
        dataset = np.random.rand(500, 96)
        self.assertEqual(len(predict_EnergyUsage(dataset)), 96)

    def test_model_training(self):
        # test output
        dataset = np.random.rand(1000, 96)
        model = predict_EnergyUsage(dataset)
        self.assertIsInstance(model, list)

    def test_future_predictions(self):
        # input is float
        dataset = np.random.rand(1000, 96)
        future_data = predict_EnergyUsage(dataset)
        # if list
        self.assertIsInstance(future_data, list)
        # if shape 96
        self.assertEqual(len(future_data), 96)
        # if it's still float
        self.assertIsInstance(future_data[0], float)


if __name__ == '__main__':
    unittest.main()
