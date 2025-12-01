from utils import string_to_binary
from codificacao import manchester_encode
from modulacao import bpsk_modulate, qpsk_modulate
from ruido import add_awgn_noise
from demodulacao import bpsk_demodulate, qpsk_demodulate, calculate_ber
from graficos import plot_ber_vs_snr
import numpy as np


def main():

    # =================== ETAPA 1 ===================
    # Em vez de mensagem pequena, cria 200 mil bits aleatórios
    N = 200000
    binary_message = ''.join(np.random.choice(['0', '1'], N))
    print("Bits gerados:", len(binary_message))

    # (Manchester opcional — não influencia BER de BPSK/QPSK)
    encoded_message = manchester_encode(binary_message[:100])  # só pra mostrar funcionamento
    print("Exemplo Manchester (100 bits):", encoded_message)

    # =================== ETAPA 2 ===================
    snr_range = range(0, 21, 2)

    ber_list_bpsk = []
    ber_list_qpsk = []

    # =================== ETAPA 3 ===================
    for snr in snr_range:

        # remodula a cada iteração (isso faz diferença estatística!)
        bpsk_signal = bpsk_modulate(binary_message)
        qpsk_signal = qpsk_modulate(binary_message)

        # adiciona AWGN correto
        noisy_b = add_awgn_noise(bpsk_signal, snr)
        noisy_q = add_awgn_noise(qpsk_signal, snr)

        # demodula
        d_bpsk = bpsk_demodulate(noisy_b)
        d_qpsk = qpsk_demodulate(noisy_q)

        # computa BER
        ber_bpsk = calculate_ber(binary_message, d_bpsk)
        ber_qpsk = calculate_ber(binary_message[:len(d_qpsk)], d_qpsk)

        ber_list_bpsk.append(ber_bpsk)
        ber_list_qpsk.append(ber_qpsk)

        print(f"SNR={snr} dB | BER BPSK={ber_bpsk:.6f} | BER QPSK={ber_qpsk:.6f}")

    # =================== ETAPA 4 ===================
    plot_ber_vs_snr(snr_range, ber_list_bpsk, ber_list_qpsk)


if __name__ == "__main__":
    main()
