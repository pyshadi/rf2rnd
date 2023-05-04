import pytest
import math
import numpy as np
import os
import sys
# Add the parent directory of both rf2rnd and tests to the sys.path list
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)
from rf2rnd import collect_rf_data, extract_random_bits

@pytest.fixture(scope="module")
def samples():
    return collect_rf_data()

def test_monobit_test(samples):
    """
    Perform the Monobit Test on the input binary sequence.

    Args:
        sequence (str): A binary sequence (string of 1s and 0s).
        significance_level (float): The significance level for the test (default: 0.01).

    Returns:
        bool: True if the sequence passes the test, False otherwise.
    """

    bits = []
    bits.append(extract_random_bits(samples, 'von_neumann_extractor'))

    n = len(bits)
    ones_count = np.count_nonzero(bits == 1)
    zeroes_count = n - ones_count

    # Calculate the test statistic (S)
    S = abs(ones_count - zeroes_count) / math.sqrt(n)

    # Calculate the P-value
    P_value = math.erfc(S / math.sqrt(2))

    # Pass the test if the P-value is greater than the significance level
    assert P_value > 0.01
