import math
import numpy as np
import pytest
from rf2rnd import collect_rf_data, extract_random_bits

def random_excursion_variant_test(samples, significance_level=0.01):
    """
    Perform the Random Excursion Variant Test on the input binary sequence.

    Args:
        samples (numpy.ndarray): Array of complex samples.
        significance_level (float): The significance level for the test (default: 0.01).

    Returns:
        bool: True if the sequence passes the test, False otherwise.
    """

    bits = extract_random_bits(samples, 'von_neumann_extractor')
    n = len(bits)

    # Calculate the cumulative sums
    S = np.cumsum((bits * 2 - 1) / np.sqrt(np.arange(1, n+1)))

    # Pad the cumulative sums with zeros
    S = np.concatenate(([0], S, [0]))

    # Define the possible states and the state counters
    states = [-4, -3, -2, -1, 1, 2, 3, 4]
    counters = dict(zip(states, [0]*len(states)))

    # Perform the random excursions
    for s in states:
        position = np.where(S == s)[0]
        for i in range(1, len(position)-1):
            j = position[i]
            x = S[j-1:j+2]
            if np.all(x == np.array([s-1, s, s+1])):
                counters[s] += 1

    # Calculate the test statistic (max absolute deviation from zero)
    V = np.max(np.abs(list(counters.values())))

    # Calculate the P-value
    P_value = math.erfc(V / math.sqrt(2 * len(bits)))
    print(f'P-value: {P_value}')
    # Pass the test if the P-value is greater than the significance level
    return P_value > significance_level


@pytest.fixture(scope="module")
def samples():
    return collect_rf_data()

def test_random_excursion_variant(samples):
    result = random_excursion_variant_test(samples)
    assert result == True

def test_random_excursion_variant_custom_significance_level(samples):
    result = random_excursion_variant_test(samples, 0.05)
    assert result == True

def test_random_excursion_variant_zeros_input():
    bits = np.zeros(1000)
    result = random_excursion_variant_test(bits)
    assert result == False

def test_random_excursion_variant_ones_input():
    bits = np.ones(1000)
    result = random_excursion_variant_test(bits)
    assert result == False
