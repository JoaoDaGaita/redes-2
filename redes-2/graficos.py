import os
import matplotlib.pyplot as plt

def plot_ber_vs_snr(snr_range, ber_values):
    """Plota o gráfico BER vs SNR e salva o gráfico em 'resultados/graficos.png'"""
    
    # Verificar se a pasta 'resultados' existe, caso contrário, criar
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
    
    plt.figure()
    plt.semilogy(snr_range, ber_values, marker='o', label='BPSK')
    plt.title('Taxa de Erro de Bit (BER) vs SNR')
    plt.xlabel('SNR (dB)')
    plt.ylabel('BER')
    plt.grid(True)
    plt.legend()
    
    # Salva o gráfico na pasta 'resultados'
    plt.savefig('resultados/graficos.png')
    plt.show()
