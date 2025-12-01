# main.py
from utils import string_to_binary
from codificacao import manchester_encode
from modulacao import bpsk_modulate, qpsk_modulate
from ruido import add_awgn_noise
from demodulacao import bpsk_demodulate, qpsk_demodulate, calculate_ber
from graficos import plot_ber_vs_snr

def run_fixed_snr_demo(message="Olá Mundo!", snr_db=10):
    print("Mensagem original:", message)
    bits = string_to_binary(message)
    print("Bits gerados:", bits)
    print("Total de bits:", len(bits))

    # codificação Manchester (string)
    encoded_bits = manchester_encode(bits)
    print("\nManchester (primeiros 80 bits):", encoded_bits[:80])
    print("Tamanho após Manchester:", len(encoded_bits))

    # MODULAÇÃO -> usando encoded_bits para modulação (após codificação)
    bpsk_sig = bpsk_modulate(encoded_bits)
    qpsk_sig = qpsk_modulate(encoded_bits)  # padding interno se necessário

    print("\nPrimeiros 10 símbolos BPSK:", bpsk_sig[:10])
    print("Primeiros 10 símbolos QPSK:", qpsk_sig[:10])

    # ADICIONAR RUÍDO
    noisy_bpsk = add_awgn_noise(bpsk_sig, snr_db)
    noisy_qpsk = add_awgn_noise(qpsk_sig, snr_db)

    print("\nPrimeiros 10 valores BPSK ruidosos:", noisy_bpsk[:10])

    # DEMODULAÇÃO
    rec_bpsk = bpsk_demodulate(noisy_bpsk)
    rec_qpsk_bits = qpsk_demodulate(noisy_qpsk)

    # Nota: rec_bpsk e rec_qpsk_bits são sequências de bits após demodulação.
    # Como usamos Manchester antes da modulação, para recuperar o texto teríamos que
    # implementar decodificação Manchester inversa — aqui calculamos BER de bits codificados.
    ber_bpsk = calculate_ber(encoded_bits, rec_bpsk)
    ber_qpsk = calculate_ber(encoded_bits, rec_qpsk_bits)

    print("\nBER (BPSK) sobre bits codificados:", ber_bpsk)
    print("BER (QPSK) sobre bits codificados:", ber_qpsk)

    return encoded_bits, bpsk_sig, qpsk_sig

def compute_ber_curve(message="Olá Mundo!"):
    bits = string_to_binary(message)
    encoded_bits = manchester_encode(bits)
    bpsk_sig = bpsk_modulate(encoded_bits)
    qpsk_sig = qpsk_modulate(encoded_bits)

    snr_range = list(range(0, 21, 2))  # 0,2,...,20 dB
    ber_bpsk = []
    ber_qpsk = []

    for snr in snr_range:
        noisy_b = add_awgn_noise(bpsk_sig, snr)
        noisy_q = add_awgn_noise(qpsk_sig, snr)

        rec_b = bpsk_demodulate(noisy_b)
        rec_q = qpsk_demodulate(noisy_q)

        ber_bpsk.append(calculate_ber(encoded_bits, rec_b))
        ber_qpsk.append(calculate_ber(encoded_bits, rec_q))

    plot_ber_vs_snr(snr_range, ber_bpsk, ber_qpsk)
    return snr_range, ber_bpsk, ber_qpsk

if __name__ == "__main__":
    run_fixed_snr_demo()
    compute_ber_curve()
