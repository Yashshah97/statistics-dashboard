import unittest
from statistics_dashboard import core

class TestCoreFunctions(unittest.TestCase):
    def test_calculate_mean(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(core.calculate_mean(data), 3)

    def test_calculate_median(self):
        data = [1, 2, 3, 4, 5]
        self.assertEqual(core.calculate_median(data), 3)

    def test_calculate_standard_deviation(self):
        data = [1, 2, 3, 4, 5]
        mean = core.calculate_mean(data)
        self.assertAlmostEqual(core.calculate_standard_deviation(data, mean), math.sqrt(2.5))

    def test_fit_distribution_constant(self):
        data = [1] * 10
        distribution_name, params = core.fit_distribution(data)
        self.assertEqual(distribution_name, "Constant")
        self.assertEqual(params["loc"], 1)

    def test_fit_distribution_exponential(self):
        data = [1 + i for i in range(10)]
        distribution_name, params = core.fit_distribution(data)
        self.assertEqual(distribution_name, "Exponential")
        self.assertAlmostEqual(params["scale"], math.sqrt(2))

if __name__ == "__main__":
    unittest.main()
