import unittest
from statistics_dashboard import utils

class TestUtils(unittest.TestCase):
    def test_calculate_mean(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(utils.calculate_mean(data), 3)

    def test_calculate_median_even_length(self):
        data = [1, 2, 3, 4]
        self.assertEqual(utils.calculate_median(data), 2.5)

    def test_calculate_median_odd_length(self):
        data = [1, 2, 3]
        self.assertEqual(utils.calculate_median(data), 2)

    def test_calculate_std_dev(self):
        data = [1, 2, 3, 4, 5]
        mean = utils.calculate_mean(data)
        self.assertAlmostEqual(utils.calculate_std_dev(data, mean), 1.4142135623730951)

    def test_calculate_covariance(self):
        x_data = [1, 2, 3, 4, 5]
        y_data = [2, 3, 5, 7, 11]
        self.assertAlmostEqual(utils.calculate_covariance(x_data, y_data), 3.0)

if __name__ == '__main__':
    unittest.main()
