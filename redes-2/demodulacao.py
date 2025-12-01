# demodulacao.py
import numpy as np

def bpsk_demodulate(noisy_signal):
    """Demodula o sinal BPSK: amostras > 0 -> '1', else '0'."""
    return ''.join('1' if sample > 0 else '0' for sample in noisy_signal)

def qpsk_demodulate(symbols):
    """Demodula símbolos QPSK conforme o mapa definido no modulador.
    Usa decisão por sinal I e Q (sinal.real > 0 => I=+1, else -1; idem para Q).
    Retorna uma string de bits (dois bits por símbolo).
    """
    bits = []
    for sym in symbols:
        r = sym.real
        i = sym.imag  # imag -> Q
        if r > 0 and i > 0:
            bits.append('00')
        elif r < 0 and i > 0:
            bits.append('01')
        elif r > 0 and i < 0:
            bits.append('10')
        else:
            bits.append('11')
    return ''.join(bits)

def calculate_ber(original_message, demodulated_message):
    """Calculo simples da BER: assume strings do mesmo comprimento (corta para o menor)."""
    L = min(len(original_message), len(demodulated_message))
    if L == 0:
        return 0.0
    errors = sum(1 for o, d in zip(original_message[:L], demodulated_message[:L]) if o != d)
    return errors / L
