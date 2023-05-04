import numpy as np
from scipy.stats import mode


def von_neumann_extractor(binary_sequence):
    """
    Generates a sequence of random bits using the Von Neumann extractor.
    Args:
        binary_sequence (numpy.ndarray): Binary sequence to extract random bits from.
    Returns:
        numpy.ndarray: Array of random bits.
    """
    random_bits = []
    for i in range(0, len(binary_sequence) - 1, 2):
        if binary_sequence[i] != binary_sequence[i + 1]:
            random_bits.append(binary_sequence[i])
    return np.array(random_bits, dtype=int)


def xor_extractor(binary_sequence):
    """
    Generates a sequence of random bits using the XOR-based extractor.
    Args:
        binary_sequence (numpy.ndarray): Binary sequence to extract random bits from.
    Returns:
        numpy.ndarray: Array of random bits.
    """
    return np.bitwise_xor(binary_sequence[:-1], binary_sequence[1:]).astype(int)


def majority_vote_extractor(binary_sequence):
    """
    Generates a sequence of random bits using the majority-vote extractor.
    Args:
        binary_sequence (numpy.ndarray): Binary sequence to extract random bits from.
    Returns:
        numpy.ndarray: Array of random bits.
    """
    bits_3d = binary_sequence[:len(binary_sequence) // 3 * 3].reshape(-1, 3)
    return mode(bits_3d, axis=1).mode.ravel().astype(int)


def bit_shift_extractor(binary_sequence):
    """
    Generates a sequence of random bits using the bit-shift extractor.
    Args:
        binary_sequence (numpy.ndarray): Binary sequence to extract random bits from.
    Returns:
        numpy.ndarray: Array of random bits.
    """
    return np.diff(binary_sequence).astype(int)


def extract_random_bits(samples, extractor_name='von_neumann_extractor'):
    """
    Extracts random bits from the given samples using the specified extractor function.
    Args:
        samples (numpy.ndarray): Array of complex samples.
        extractor_name (str): Name of the function to use for extracting random bits. Default is 'von_neumann_extractor'.
    Returns:
        numpy.ndarray: Array of random bits.
    """
    extractors = {
        'von_neumann_extractor': von_neumann_extractor,
        'xor_extractor': xor_extractor,
        'majority_vote_extractor': majority_vote_extractor,
        'bit_shift_extractor': bit_shift_extractor
    }

    # Convert the complex samples to floats and normalize them
    normalized_samples = np.abs(samples) / np.max(np.abs(samples))
    # Apply a threshold to the samples to generate a binary sequence
    threshold = 0.5
    binary_sequence = (normalized_samples > threshold).astype(int)

    # Use the specified extractor function to generate a sequence of random bits
    extractor = extractors.get(extractor_name, von_neumann_extractor)
    random_bits = extractor(binary_sequence)

    return random_bits
