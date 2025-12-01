def string_to_binary(message):
    """Converte uma string para binário no formato ASCII"""
    return ''.join(format(ord(c), '08b') for c in message)
