import re

def validar_numero_telefone(numero):
    # Expressão regular para validar números de telefone no formato brasileiro
    # (XX) 9XXXX-XXXX, onde X é um dígito de 0 a 9
    regex = re.compile(r'^\(\d{2}\) 9\d{4}-\d{4}$')

    # Verifica se o número corresponde à expressão regular
    if regex.match(numero):
        return True
    else:
        return False