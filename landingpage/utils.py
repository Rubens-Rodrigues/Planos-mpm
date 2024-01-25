import re

def validar_numero_telefone(numero):
    # Expressão regular para validar números de telefone no formato brasileiro
    # (XX) 9XXXX-XXXX, onde X é um dígito de 0 a 9
    regex = re.compile(r'^\(\d{2}\) 9\d{4}-\d{4}$')

    # Verifica se o número corresponde à expressão regular
    if not regex.match(numero):
        return False

     # Verifica se há mais de 4 dígitos consecutivos repetidos
    repeticoes_maximas = 4
    for i in range(len(numero) - repeticoes_maximas):
        if len(set(numero[i:i + repeticoes_maximas + 1])) == 1:
            return False

    return True