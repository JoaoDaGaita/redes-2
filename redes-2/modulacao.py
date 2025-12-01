# modulacao.py
import numpy as np

def bpsk_modulate(binary_message):
    """Modula a mensagem em BPSK: '1' -> +1, '0' -> -1 (retorna np.array float)."""
    return np.array([1.0 if bit == '1' else -1.0 for bit in binary_message])

def qpsk_modulate(binary_message):
    """Modula a mensagem em QPSK (mapa dado por você).
    Recebe uma string de bits; se comprimento ímpar, adiciona '0' no final.
    Retorna np.array de complexos (I + jQ).
    """
    bits = binary_message
    if len(bits) % 2 != 0:
        bits = bits + '0'  # padding

    symbols = []
    for i in range(0, len(bits), 2):
        pair = bits[i:i+2]
        if pair == '00':
            symbols.append(1 + 1j)
        elif pair == '01':
            symbols.append(-1 + 1j)
        elif pair == '10':
            symbols.append(1 - 1j)
        else:  # '11'
            symbols.append(-1 - 1j)
    return np.array(symbols, dtype=complex)
