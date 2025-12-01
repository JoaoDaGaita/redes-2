# ruido.py
import numpy as np

def add_awgn_noise(signal, snr_db):
    """Adiciona ruído AWGN ao sinal (suporta sinais reais e complexos).
    snr_db é SNR por símbolo em dB.
    """
    # potência média do sinal
    signal_power = np.mean(np.abs(signal)**2)
    # converter SNR dB -> linear
    snr_linear = 10**(snr_db / 10.0)
    # potência do ruído (por amostra)
    noise_power = signal_power / snr_linear

    # se sinal é complexo, o ruído deve ser complexo com variance/2 em cada eixo
    if np.iscomplexobj(signal):
        noise = np.sqrt(noise_power/2) * (np.random.randn(len(signal)) + 1j * np.random.randn(len(signal)))
    else:
        noise = np.sqrt(noise_power) * np.random.randn(len(signal))

    return signal + noise
