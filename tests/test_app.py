import unittest
from statistics_dashboard import app

class TestApp(unittest.TestCase):

    def test_parse_args(self):
        args = app.parser.parse_args(['--version'])
        self.assertEqual(args.version, __version__)

    def test_version_string(self):
        version_str = app.__version__
        self.assertIsInstance(version_str, str)

if __name__ == '__main__':
    unittest.main()
