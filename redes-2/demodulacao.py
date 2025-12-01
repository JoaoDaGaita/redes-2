def bpsk_demodulate(noisy_signal):
    """Demodula o sinal BPSK"""
    return ''.join('1' if sample > 0 else '0' for sample in noisy_signal)

def calculate_ber(original_message, demodulated_message):
    """Calcula a Taxa de Erro de Bit (BER)"""
    errors = sum(1 for o, d in zip(original_message, demodulated_message) if o != d)
    return errors / len(original_message)
