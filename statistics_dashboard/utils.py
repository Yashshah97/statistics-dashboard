"""
Utility functions used across the application.

This module contains utility functions that are used by multiple parts of the
application. It is kept separate to avoid polluting other modules with these
functions.
"""

import math
from typing import List, Tuple

def calculate_mean(data: List[float]) -> float:
    """
    Calculate the mean of a list of numbers.

    Args:
        data (List[float]): The list of numbers.

    Returns:
        float: The mean of the list.
    """
    return sum(data) / len(data)

def calculate_median(data: List[float]) -> float:
    """
    Calculate the median of a list of numbers.

    Args:
        data (List[float]): The list of numbers.

    Returns:
        float: The median of the list.
    """
    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

def calculate_std_dev(data: List[float], mean: float) -> float:
    """
    Calculate the standard deviation of a list of numbers.

    Args:
        data (List[float]): The list of numbers.
        mean (float): The mean of the list.

    Returns:
        float: The standard deviation of the list.
    """
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return math.sqrt(variance)

def calculate_covariance(x_data: List[float], y_data: List[float]) -> float:
    """
    Calculate the covariance between two lists of numbers.

    Args:
        x_data (List[float]): The first list of numbers.
        y_data (List[float]): The second list of numbers.

    Returns:
        float: The covariance between the two lists.
    """
    mean_x = calculate_mean(x_data)
    mean_y = calculate_mean(y_data)

    numerator = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_data, y_data))
    denominator = len(x_data)

    return numerator / denominator
