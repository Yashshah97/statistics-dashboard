import unittest
from statistics_dashboard import models

class TestModels(unittest.TestCase):

    def test_distribution_init(self):
        dist = models.Distribution('Normal', {'mean': 0, 'std_dev': 1})
        self.assertEqual(dist.name, 'Normal')
        self.assertEqual(dist.params['mean'], 0)
        self.assertEqual(dist.params['std_dev'], 1)

    def test_hypothesis_test_init(self):
        test = models.HypothesisTest('t-test', {'sample_size': 100, 'significance_level': 0.05})
        self.assertEqual(test.name, 't-test')
        self.assertEqual(test.params['sample_size'], 100)
        self.assertEqual(test.params['significance_level'], 0.05)

    def test_data_point_init(self):
        dist = models.Distribution('Normal', {'mean': 0, 'std_dev': 1})
        data_point = models.DataPoint(10.5, dist)
        self.assertEqual(data_point.value, 10.5)
        self.assertEqual(data_point.distribution.name, 'Normal')

    def test_statistic_init(self):
        stat = models.Statistic('mean', 10.5, {'sample_size': 100})
        self.assertEqual(stat.name, 'mean')
        self.assertEqual(stat.result, 10.5)
        self.assertEqual(stat.params['sample_size'], 100)

    def test_sparkline_init(self):
        dist = models.Distribution('Normal', {'mean': 0, 'std_dev': 1})
        data_points = [models.DataPoint(10.5, dist), models.DataPoint(20.5, dist)]
        sparkline = models.Sparkline(data_points, dist)
        self.assertEqual(len(sparkline.data_points), 2)
        self.assertEqual(sparkline.distribution.name, 'Normal')

    def test_panel_init(self):
        stat1 = models.Statistic('mean', 10.5, {'sample_size': 100})
        stat2 = models.Statistic('median', 20.5, {'sample_size': 100})
        panel = models.Panel('Statistics', [(stat1.name, stat1), (stat2.name, stat2)])
        self.assertEqual(panel.title, 'Statistics')
        self.assertEqual(len(panel.content), 2)

if __name__ == '__main__':
    unittest.main()
