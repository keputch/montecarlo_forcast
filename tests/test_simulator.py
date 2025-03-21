# tests/test_simulator.py

import pytest
from ..engine.simulator import monte_carlo_throughput, \
                               monte_carlo_delivery_date, \
                               calculate_percentile_summary, \
                               probability_of_value_or_less

def test_throughput_forecast_returns_expected_simulation_runs():
    cycle_times = [3, 5, 2, 4, 6]
    days = 10
    simulations = 1000

    results = monte_carlo_throughput(cycle_times, days, simulations)

    assert len(results) == simulations
    assert all(isinstance(x, int) and x >= 0 for x in results)

def test_delivery_forecast_returns_expected_simulation_runs():
    cycle_times = [3, 5, 2, 4, 6]
    items = 20
    simulations = 1000

    results = monte_carlo_delivery_date(cycle_times, items, simulations)

    assert len(results) == simulations
    assert all(isinstance(x, int) and x > 0 for x in results)

def test_percentile_summary_and_probability_helpers():
    results = list(range(1, 101))  # 1–100

    summary = calculate_percentile_summary(results, percentiles=[50, 90])
    assert summary["P50"] == 50.5
    assert summary["P90"] == pytest.approx(90.1, abs=0.1)

    prob = probability_of_value_or_less(results, 80)
    assert prob == 80.0
