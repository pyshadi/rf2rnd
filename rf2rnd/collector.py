""" Collect RF samples using SDR receiver"""
import rtlsdr
import numpy as np

def collect_rf_data(center_freq=20e6, sample_rate=2.4e6, gain=20, num_samples=1024):
    """
    Collects RF noise data using an SDR receiver.
    Args:
        center_freq (float): Center frequency in Hz.
        sample_rate (float): Sample rate in Hz.
        gain (int): Gain in dB.
        num_samples (int): Number of samples to collect.
    Returns:
        numpy.ndarray: Array of complex samples.
    """

    sdr = rtlsdr.RtlSdr()
    sdr.set_center_freq(center_freq)
    sdr.set_sample_rate(sample_rate)
    sdr.set_gain(gain)
    samples = sdr.read_samples(num_samples)
    sdr.close()
    return samples


def collect_hopping_rf_data(center_freqs=None, sample_rate=2.4e6, gain=20, num_samples=1024, hop_interval=32):
    """
    Collects RF noise data using an SDR receiver with frequency hopping.
    Args:
        center_freqs (list): List of center frequencies to hop between in Hz. Default is None, which hops between 20 MHz to 30 MHz.
        sample_rate (float): Sample rate in Hz.
        gain (int): Gain in dB.
        num_samples (int): Number of samples to collect.
        hop_interval (int): Number of samples to collect at each frequency before hopping to the next one.
    Returns:
        numpy.ndarray: Array of complex samples.
    """
    if center_freqs is None:
        # Default to hopping between 20 MHz to 30 MHz with a step size of 0.1 MHz
        center_freqs = np.arange(20e6, 30e6, 0.1e6)

    num_freqs = len(center_freqs)
    freq_idx = 0
    samples = np.array([], dtype=np.complex128)
    sdr = rtlsdr.RtlSdr()
    sdr.set_sample_rate(sample_rate)
    sdr.set_gain(gain)

    while len(samples) < num_samples:
        center_freq = center_freqs[freq_idx % num_freqs]
        sdr.set_center_freq(center_freq)
        curr_samples = sdr.read_samples(hop_interval)
        samples = np.concatenate([samples, curr_samples])
        freq_idx += 1

    sdr.close()
    return samples[:num_samples]
