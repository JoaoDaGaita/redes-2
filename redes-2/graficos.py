import os
import matplotlib.pyplot as plt

def plot_ber_vs_snr(snr_range, ber_bpsk, ber_qpsk):
    """Plota o gráfico BER vs SNR para BPSK e QPSK"""

    if not os.path.exists("resultados"):
        os.makedirs("resultados")

    plt.figure()
    plt.semilogy(snr_range, ber_bpsk, marker='o', label='BPSK')
    plt.semilogy(snr_range, ber_qpsk, marker='s', label='QPSK')

    plt.title("BER vs SNR (BPSK vs QPSK)")
    plt.xlabel("SNR (dB)")
    plt.ylabel("BER")
    plt.grid(True)
    plt.legend()

    plt.savefig("resultados/ber_comparacao.png")
    plt.show()
