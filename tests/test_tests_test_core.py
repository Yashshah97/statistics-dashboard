import unittest
from statistics_dashboard import tests_test_core

class TestTestCore(unittest.TestCase):

    def test_distribution_fitting(self) -> None:
        """
        Test the `test_distribution_fitting` function.
        """
        # Run the original test and assert that it doesn't raise any exceptions
        try:
            tests_test_core.test_distribution_fitting()
        except AssertionError as e:
            self.fail(f"Test failed with assertion error: {e}")

    def test_hypothesis_testing(self) -> None:
        """
        Test the `test_hypothesis_testing` function.
        """
        # Run the original test and assert that it doesn't raise any exceptions
        try:
            tests_test_core.test_hypothesis_testing()
        except AssertionError as e:
            self.fail(f"Test failed with assertion error: {e}")

if __name__ == '__main__':
    unittest.main()
