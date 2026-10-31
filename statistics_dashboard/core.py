"""
Core functionality for distribution fitting and hypothesis tests.

This module provides functions and classes for performing statistical analysis,
including distribution fitting and hypothesis testing.
"""

import math
from typing import Callable, Dict, List, Tuple

def calculate_mean(data: List[float]) -> float:
    """
    Calculate the mean of a list of numbers.

    Args:
        data (List[float]): The input data.

    Returns:
        float: The mean of the input data.
    """
    return sum(data) / len(data)

def calculate_median(data: List[float]) -> float:
    """
    Calculate the median of a list of numbers.

    Args:
        data (List[float]): The input data.

    Returns:
        float: The median of the input data.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

def calculate_standard_deviation(data: List[float], mean: float) -> float:
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        data (List[float]): The input data.
        mean (float): The mean of the input data.

    Returns:
        float: The standard deviation of the input data.
    """
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

def fit_distribution(data: List[float]) -> Tuple[str, Dict]:
    """
    Fit a distribution to a list of numbers.

    Args:
        data (List[float]): The input data.

    Returns:
        Tuple[str, Dict]: A tuple containing the name of the fitted distribution
            and its parameters.
    """
    mean = calculate_mean(data)
    median = calculate_median(data)
    std_dev = calculate_standard_deviation(data, mean)

    if len(set(data)) == 1:
        return "Constant", {"loc": data[0]}
    elif all(x > 0 for x in data):
        return "Exponential", {"scale": std_dev}
    else:
        return "Normal", {"loc": mean, "scale": std_dev}

def perform_hypothesis_test(data: List[float], null_mean: float) -> Tuple[str, float]:
    """
    Perform a hypothesis test on a list of numbers.

    Args:
        data (List[float]): The input data.
        null_mean (float): The null hypothesis mean.

    Returns:
        Tuple[str, float]: A tuple containing the result of the hypothesis test
            and its p-value.
    """
    t_statistic = calculate_t_statistic(data, null_mean)
    degrees_of_freedom = len(data) - 1

    if abs(t_statistic) > math.sqrt(degrees_of_freedom):
        return "Reject", 0.0
    else:
        return "Fail to reject", 1.0

def calculate_t_statistic(data: List[float], null_mean: float) -> float:
    """
    Calculate the t-statistic for a list of numbers.

    Args:
        data (List[float]): The input data.
        null_mean (float): The null hypothesis mean.

    Returns:
        float: The t-statistic.
    """
    mean = calculate_mean(data)
    std_dev = calculate_standard_deviation(data, mean)

    return (mean - null_mean) / (std_dev / math.sqrt(len(data)))
