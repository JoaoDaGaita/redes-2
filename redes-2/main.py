from utils import string_to_binary
from codificacao import manchester_encode
from modulacao import bpsk_modulate, qpsk_modulate
from ruido import add_awgn_noise
from demodulacao import bpsk_demodulate, calculate_ber
from graficos import plot_ber_vs_snr

def main():
    # Etapa 1: Gerar a mensagem e convertê-la em binário
    message = "Olá Mundo!"
    binary_message = string_to_binary(message)
    print(f'Mensagem binária: {binary_message}')
    
    # Etapa 2: Codificar a mensagem
    encoded_message = manchester_encode(binary_message)
    print(f'Mensagem codificada Manchester: {encoded_message}')
    
    # Etapa 3: Modulação (BPSK e QPSK)
    bpsk_signal = bpsk_modulate(binary_message)
    qpsk_signal = qpsk_modulate(binary_message)
    
    # Etapa 4: Adicionar ruído AWGN
    noisy_bpsk_signal = add_awgn_noise(bpsk_signal, snr_db=10)
    
    # Etapa 5: Demodular o sinal
    demodulated_message_bpsk = bpsk_demodulate(noisy_bpsk_signal)
    print(f'Mensagem demodulada BPSK: {demodulated_message_bpsk}')
    
    # Etapa 6: Calcular e exibir a BER
    ber = calculate_ber(binary_message, demodulated_message_bpsk)
    print(f'BER: {ber}')
    
    # Etapa 7: Plotar gráfico BER vs SNR
    snr_range = range(0, 21, 2)
    ber_values = [calculate_ber(binary_message, bpsk_demodulate(add_awgn_noise(bpsk_signal, snr))) for snr in snr_range]
    plot_ber_vs_snr(snr_range, ber_values)

if __name__ == '__main__':
    main()
