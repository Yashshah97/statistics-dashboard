"""
Data models and structures used throughout the application.

This module defines data classes for distribution fitting and hypothesis tests,
used to store and manipulate data in a structured way.
"""

from typing import Dict, List, Tuple

class Distribution:
    """
    Represents a statistical distribution with its parameters.

    Attributes:
        name (str): Name of the distribution (e.g. 'Normal', 'Exponential').
        params (Dict[str, float]): Parameters of the distribution (e.g. mean, std dev).
    """

    def __init__(self, name: str, params: Dict[str, float]):
        self.name = name
        self.params = params

class HypothesisTest:
    """
    Represents a hypothesis test with its parameters.

    Attributes:
        name (str): Name of the test (e.g. 't-test', 'chi-squared').
        params (Dict[str, float]): Parameters of the test (e.g. sample size, significance level).
    """

    def __init__(self, name: str, params: Dict[str, float]):
        self.name = name
        self.params = params

class DataPoint:
    """
    Represents a single data point with its value and distribution.

    Attributes:
        value (float): Value of the data point.
        distribution (Distribution): Distribution that this data point belongs to.
    """

    def __init__(self, value: float, distribution: Distribution):
        self.value = value
        self.distribution = distribution

class Statistic:
    """
    Represents a statistical calculation with its result and parameters.

    Attributes:
        name (str): Name of the statistic (e.g. 'mean', 'median').
        result (float): Result of the calculation.
        params (Dict[str, float]): Parameters of the calculation (e.g. sample size).
    """

    def __init__(self, name: str, result: float, params: Dict[str, float]):
        self.name = name
        self.result = result
        self.params = params

class Sparkline:
    """
    Represents a sparkline with its data points and distribution.

    Attributes:
        data_points (List[DataPoint]): Data points that make up the sparkline.
        distribution (Distribution): Distribution that these data points belong to.
    """

    def __init__(self, data_points: List[DataPoint], distribution: Distribution):
        self.data_points = data_points
        self.distribution = distribution

class Panel:
    """
    Represents a panel with its title and content.

    Attributes:
        title (str): Title of the panel.
        content (List[Tuple[str, Statistic]]): Content of the panel as a list of tuples.
    """

    def __init__(self, title: str, content: List[Tuple[str, Statistic]]):
        self.title = title
        self.content = content
