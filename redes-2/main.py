from utils import string_to_binary
from codificacao import manchester_encode
from modulacao import bpsk_modulate, qpsk_modulate
from ruido import add_awgn_noise
from demodulacao import bpsk_demodulate, qpsk_demodulate, calculate_ber
from graficos import plot_ber_vs_snr


def main():
    # =================== ETAPA 1 ===================
    message = "Olá Mundo!"
    binary_message = string_to_binary(message)
    print("Bits gerados:", binary_message)

    # =================== ETAPA 2 ===================
    encoded_message = manchester_encode(binary_message)
    print("Mensagem codificada Manchester:", encoded_message)

    # =================== ETAPA 3 ===================
    bpsk_signal = bpsk_modulate(binary_message)
    qpsk_signal = qpsk_modulate(binary_message)

    # =================== ETAPA 4 ===================
    noisy_bpsk = add_awgn_noise(bpsk_signal, snr_db=10)
    noisy_qpsk = add_awgn_noise(qpsk_signal, snr_db=10)

    # =================== ETAPA 5 ===================
    demod_bpsk = bpsk_demodulate(noisy_bpsk)
    demod_qpsk = qpsk_demodulate(noisy_qpsk)

    # =================== ETAPA 6 ===================
    ber_bpsk = calculate_ber(binary_message, demod_bpsk)
    ber_qpsk = calculate_ber(binary_message[:len(demod_qpsk)], demod_qpsk)

    print(f"BER BPSK: {ber_bpsk}")
    print(f"BER QPSK: {ber_qpsk}")

    # =================== ETAPA 7 ===================
    snr_range = range(0, 21, 2)

    ber_list_bpsk = []
    ber_list_qpsk = []

    for snr in snr_range:
        noisy_b = add_awgn_noise(bpsk_signal, snr)
        noisy_q = add_awgn_noise(qpsk_signal, snr)

        d_bpsk = bpsk_demodulate(noisy_b)
        d_qpsk = qpsk_demodulate(noisy_q)

        ber_list_bpsk.append(calculate_ber(binary_message, d_bpsk))
        ber_list_qpsk.append(calculate_ber(binary_message[:len(d_qpsk)], d_qpsk))

    plot_ber_vs_snr(snr_range, ber_list_bpsk, ber_list_qpsk)


if __name__ == "__main__":
    main()
