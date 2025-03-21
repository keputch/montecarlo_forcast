# engine/simulator.py

# engine/simulator.py

import random
import numpy as np
from collections import Counter


def monte_carlo_throughput(cycle_times, num_days, num_simulations):
    """
    Simulate how many items can be completed in num_days.
    """
    results = []

    for _ in range(num_simulations):
        days_spent = 0
        items_delivered = 0

        while days_spent < num_days:
            cycle_time = random.choice(cycle_times)
            if days_spent + cycle_time > num_days:
                break
            days_spent += cycle_time
            items_delivered += 1

        results.append(items_delivered)

    return results


def monte_carlo_delivery_date(cycle_times, num_items, num_simulations):
    """
    Simulate how many days it takes to deliver a fixed number of items.
    """
    results = []

    for _ in range(num_simulations):
        total_days = 0
        for _ in range(num_items):
            cycle_time = random.choice(cycle_times)
            total_days += cycle_time
        results.append(total_days)

    return results


def calculate_percentile_summary(results, percentiles=[50, 70, 85, 95]):
    """
    Calculate percentile summary from simulation results.
    Example: 85% probability the result is <= X.
    """
    summary = {}
    for p in percentiles:
        summary[f"P{p}"] = np.percentile(results, p)
    return summary


def probability_of_value_or_less(results, value):
    """
    Calculates the probability that a simulation result is <= value.
    """
    count = sum(1 for x in results if x >= value)
    probability = count / len(results)
    return round(probability * 100, 2)

