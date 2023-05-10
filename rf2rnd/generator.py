from rf2rnd import extract_random_bits
import numpy as np
def lcg(seed, a, c, m):
    """Linear Congruential Generator."""
    return (a * seed + c) % int(m)

def randflo(samples, num_numbers=1, low=0., high=1000.):

    """
    Generates a list of random floats between a low and high value using a Linear Congruential Generator (LCG).
    :param samples: number of random bits to extract from the input source
    :param num_numbers: number of random floats to generate (default: 1)
    :param low: the minimum value for the random floats (default: 0.0)
    :param high: the maximum value for the random floats (default: 1000.0)
    :return: a list of random floats
    """

    bits = extract_random_bits(samples)
    ints = bits.astype(int)

    # Use the first extracted bit as the initial seed
    seed = np.uint64(ints[0])

    # LCG parameters (choose carefully to ensure a long period and good randomness)
    a = 1103515245
    c = 12345
    m = 2 ** 31 - 1

    random_floats = []
    for _ in range(num_numbers):
        seed = lcg(seed, a, c, m)
        random_floats.append(low + ((seed % (10**9)) / (10**9)) * (high - low))

    return random_floats


def randint(samples, num_numbers=1, low=0, high=1000):
    """
    Generates a list of random integers between a low and high value using a Linear Congruential Generator (LCG).
    :param samples: number of random bits to extract from the input source
    :param num_numbers: number of random integers to generate (default: 1)
    :param low: the minimum value for the random integers (default: 0)
    :param high: the maximum value for the random integers (default: 1000)
    :return: a list of random integers
    """

    bits = extract_random_bits(samples)
    ints = bits.astype(int)

    # Use the first extracted bit as the initial seed
    seed = np.uint64(ints[0])

    # LCG parameters (choose carefully to ensure a long period and good randomness)
    a = 1103515245
    c = 12345
    m = 2 ** 31 - 1

    random_ints = []
    for _ in range(num_numbers):
        seed = lcg(seed, a, c, m)
        random_ints.append(low + (seed % (high - low)))

    return random_ints