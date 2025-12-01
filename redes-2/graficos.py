# graficos.py
import os
import matplotlib.pyplot as plt
import numpy as np

def plot_ber_vs_snr(snr_range, ber_bpsk, ber_qpsk=None, filename='resultados/ber_vs_snr.png'):
    """Plota BER vs SNR. Se ber_qpsk for fornecido, plota comparação BPSK x QPSK."""
    if not os.path.exists('resultados'):
        os.makedirs('resultados')

    plt.figure()
    plt.semilogy(snr_range, ber_bpsk, marker='o', label='BPSK')
    if ber_qpsk is not None:
        plt.semilogy(snr_range, ber_qpsk, marker='s', label='QPSK')
    plt.title('Taxa de Erro de Bit (BER) vs SNR')
    plt.xlabel('SNR (dB)')
    plt.ylabel('BER')
    plt.grid(True)
    plt.legend()
    plt.savefig(filename)
    plt.show()
