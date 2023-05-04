import numpy as np
import os
import sys
import matplotlib.pyplot as plt

# Add the parent directory of both rf2rnd and tests to the sys.path list
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from rf2rnd import collect_rf_data, extract_random_bits, randflo, randint

def entropy_test(numbers):
    """
    Computes the Shannon entropy of a sequence of numbers.

    Args:
        numbers (numpy.ndarray): Array of numbers.

    Returns:
        float: Shannon entropy of the sequence of numbers.
    """
    # Check if numbers is already a numpy array
    if not isinstance(numbers, np.ndarray):
        numbers = np.array(numbers)

    # Compute the frequency of each number in the sequence
    unique, counts = np.unique(numbers, return_counts=True)
    freqs = counts / len(numbers)

    # Compute the Shannon entropy of the sequence
    entropy = -np.sum(freqs * np.log2(freqs))

    return entropy

def test_random_numbers(samples, num_numbers, low, high):
    """
    Generates random numbers from the given samples within the given range and performs an entropy test.
    Args:
        samples (numpy.ndarray): Array of complex samples.
        num_numbers (int): Number of random numbers to generate.
        low (int): Lowest value for the random numbers to be generated.
        high (int): Highest value for the random numbers to be generated.
    Returns:
        tuple: Tuple containing the generated random numbers, their entropy, and the entropy of `numpy` random numbers.
    """

    bits = extract_random_bits(samples)
    rnd_entropies = []
    np_entropies = []
    random_numbers = list(range(low, high+1))

    for i in random_numbers:
        rn = randint(bits, num_numbers, low, i)
        entropy = entropy_test(rn)
        rnd_entropies.append(entropy)
        numpy_numbers = np.random.randint(low, high, size=i, dtype=np.uint64)
        np_entropy = entropy_test(numpy_numbers)
        np_entropies.append(np_entropy)




    # Plot the entropy range of generated random numbers versus entropy value
    plt.plot(random_numbers, rnd_entropies, label='Generated Random Numbers')
    plt.plot(random_numbers, np_entropies, label='Numpy Random Numbers')
    plt.xlabel('Range of random numbers')
    plt.ylabel('Entropy')
    plt.title('Entropy Test')
    plt.legend()
    plt.show()

def main():
    samples = collect_rf_data()
    test_random_numbers(samples, 10000, 0, 1000)

if __name__ == "__main__":
    main()