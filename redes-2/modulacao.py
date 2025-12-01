import numpy as np

def bpsk_modulate(binary_message):
    """Modula a mensagem em BPSK"""
    return np.array([1 if bit == '1' else -1 for bit in binary_message])

def qpsk_modulate(binary_message):
    """Modula a mensagem em QPSK"""
    symbols = []
    for i in range(0, len(binary_message), 2):
        bits = binary_message[i:i+2]
        if bits == '00':
            symbols.append(1 + 1j)  # 00 -> 1 + j
        elif bits == '01':
            symbols.append(-1 + 1j)  # 01 -> -1 + j
        elif bits == '10':
            symbols.append(1 - 1j)  # 10 -> 1 - j
        else:
            symbols.append(-1 - 1j)  # 11 -> -1 - j
    return np.array(symbols)
