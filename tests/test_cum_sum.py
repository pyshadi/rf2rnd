import math
import numpy as np
import os
import sys
# Add the parent directory of both rf2rnd and tests to the sys.path list
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from rf2rnd import collect_rf_data, extract_random_bits


def test_cumulative_sums_test():
    samples = collect_rf_data()
    bits = extract_random_bits(samples, 'von_neumann_extractor')
    n = len(bits)

    # Calculate the cumulative sums
    S = np.cumsum((bits * 2 - 1) / np.sqrt(np.arange(1, n+1)))

    # Calculate the test statistic (max absolute deviation from zero)
    V = np.max(np.abs(S))

    # Calculate the P-value
    P_value = math.erfc(V / math.sqrt(2 * n))

    # Test passes if the P-value is greater than 0.01
    assert P_value > 0.01, f"Failed with P-value: {P_value}"

