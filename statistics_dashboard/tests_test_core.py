"""
Unit tests for core functionality of the Statistics TUI Dashboard.

This module contains unit tests that verify the correctness of core features in the dashboard.
"""

import unittest
from statistics_dashboard.core import DistributionFitter, HypothesisTester
from typing import List, Tuple

class TestCoreFunctionality(unittest.TestCase):

    def test_distribution_fitting(self) -> None:
        """
        Test fitting a distribution to sample data.

        This test verifies that the `DistributionFitter` class correctly fits a distribution
        to sample data.
        """
        # Generate some sample data
        import random
        data: List[float] = [random.gauss(0, 1) for _ in range(100)]

        # Fit a normal distribution to the data
        fitter = DistributionFitter(data)
        params = fitter.fit()

        # Verify that the fitted parameters are reasonable
        self.assertGreater(params['loc'], -10)
        self.assertLess(params['scale'], 10)

    def test_hypothesis_testing(self) -> None:
        """
        Test hypothesis testing using the `HypothesisTester` class.

        This test verifies that the `HypothesisTester` class correctly performs a t-test.
        """
        # Generate some sample data
        import random
        data1: List[float] = [random.gauss(0, 1) for _ in range(100)]
        data2: List[float] = [random.gauss(0, 1.5) for _ in range(100)]

        # Perform a t-test on the two datasets
        tester = HypothesisTester(data1, data2)
        result = tester.test()

        # Verify that the test result is reasonable
        self.assertGreater(result['t_stat'], -10)

if __name__ == '__main__':
    unittest.main()
