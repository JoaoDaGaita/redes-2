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

    # 👉 AQUI você mostra os bits gerados
    print("===== ETAPA 1: Bits gerados (ASCII) =====")
    print(binary_message)
    print(f"Total de bits: {len(binary_message)}\n")
    
    # Etapa 2: Codificar a mensagem
    encoded_message = manchester_encode(binary_message)
    print("===== ETAPA 2: Codificação Manchester =====")
    print(encoded_message)
    print(f"Tamanho após codificação: {len(encoded_message)} símbolos\n")
    
    # Etapa 3: Modulação (BPSK e QPSK)
    bpsk_signal = bpsk_modulate(binary_message)
    qpsk_signal = qpsk_modulate(binary_message)

    print("===== ETAPA 3: Modulação =====")
    print("Primeiros 10 símbolos BPSK:", bpsk_signal[:10])
    print("Primeiros 10 símbolos QPSK:", qpsk_signal[:10], "\n")
    
    # Etapa 4: Adicionar ruído AWGN
    noisy_bpsk_signal = add_awgn_noise(bpsk_signal, snr_db=10)
    print("===== ETAPA 4: Canal AWGN =====")
    print("Primeiros 10 valores do sinal BPSK ruidoso:", noisy_bpsk_signal[:10], "\n")
    
    # Etapa 5: Demodular o sinal
    demodulated_message_bpsk = bpsk_demodulate(noisy_bpsk_signal)
    print("===== ETAPA 5: Demodulação =====")
    print(demodulated_message_bpsk, "\n")
    
    # Etapa 6: Calcular e exibir a BER
    ber = calculate_ber(binary_message, demodulated_message_bpsk)
    print("===== ETAPA 6: BER =====")
    print(f'BER: {ber}\n')
    
    # Etapa 7: Plotar gráfico BER vs SNR
    print("===== ETAPA 7: Gerando gráfico BER vs SNR =====")
    snr_range = range(0, 21, 2)
    ber_values = [
        calculate_ber(binary_message, 
                      bpsk_demodulate(add_awgn_noise(bpsk_signal, snr))) 
        for snr in snr_range
    ]
    plot_ber_vs_snr(snr_range, ber_values)

if __name__ == '__main__':
    main()
