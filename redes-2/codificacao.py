import numpy as np

def manchester_encode(binary_message):
    """Codifica a mensagem em Manchester"""
    encoded_signal = []
    for bit in binary_message:
        if bit == '1':
            encoded_signal.extend([1, 0])  # 1 -> 01
        else:
            encoded_signal.extend([0, 1])  # 0 -> 10
    return np.array(encoded_signal)
