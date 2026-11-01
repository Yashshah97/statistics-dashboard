"""Smoke tests for app."""
import unittest

from statistics_dashboard import app


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(app, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(app) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
