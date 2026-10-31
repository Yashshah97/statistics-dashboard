import unittest
from statistics_dashboard import dashboard

class TestDashboard(unittest.TestCase):
    def test_init(self):
        dash = dashboard.Dashboard()
        self.assertEqual(dash.panels, {})

    def test_add_panel(self):
        dash = dashboard.Dashboard()
        dash.add_panel('panel1')
        self.assertIn('panel1', dash.panels)
        self.assertEqual(dash.panels['panel1'], {'y': 0, 'x': 0})

    def test_update_panel_defaults(self):
        dash = dashboard.Dashboard()
        dash.add_panel('panel1')
        dash.update_panel('panel1')
        panel = dash.panels['panel1']
        self.assertEqual(panel['height'], 1)
        self.assertEqual(panel['width'], 20)

    def test_update_panel_values(self):
        dash = dashboard.Dashboard()
        dash.add_panel('panel1')
        dash.update_panel('panel1', height=10, width=30)
        panel = dash.panels['panel1']
        self.assertEqual(panel['height'], 10)
        self.assertEqual(panel['width'], 30)

if __name__ == '__main__':
    unittest.main()
