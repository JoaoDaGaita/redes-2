import numpy as np

def add_awgn_noise(signal, snr_db):
    """Adiciona ruído AWGN ao sinal"""
    signal_power = np.mean(np.abs(signal)**2)
    snr_linear = 10**(snr_db / 10)
    noise_power = signal_power / snr_linear
    noise = np.sqrt(noise_power) * np.random.randn(len(signal))
    return signal + noise
