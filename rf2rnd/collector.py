""" Collect RF samples using SDR receiver"""
import rtlsdr

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

