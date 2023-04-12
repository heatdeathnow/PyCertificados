from unidecode import unidecode


def name(x):
    return unidecode(x.upper())


def cpf(x):
    # Transforma variável em string e retira pontos, hifens e traços se tiver.
    x = str(x).replace('.', '').replace('-', '').replace('/', '')

    # Se tiver faltando números no CPF, adiciona zeros no começo.
    if len(x) < 11:
        x = '0' * (11 - len(x)) + x

    elif len(x) > 11:
        raise Exception(f'CPF {x} tem caracteres demais')

    # Formata e retorna o CPF.
    return x[:3] + '.' + x[3:6] + '.' + x[6:9] + '-' + x[9:]


def cnpj(x):
    # Transforma variável em string e retira pontos, hifens e traços se tiver.
    x = str(x).replace('.', '').replace('-', '').replace('/', '')

    # Se tiver faltando números no CNPJ, adiciona zeros no começo.
    if len(x) < 14:
        x = '0' * (14 - len(x)) + x

    elif len(x) <= 15:
        x = x.replace('0', '', 1)

    else:
        raise Exception(f'CNPJ {x} tem caracteres demais')

    # Formata e retorna o CNPJ.
    return x[:2] + '.' + x[2:5] + '.' + x[5:8] + '/' + x[8:12] + '-' + x[12:]


def matr(x):
    x = str(x)

    if len(x) < 6:
        x = '0' * (6 - len(x)) + x

    elif len(x) > 6:
        raise Exception(f'Matrícula {x} tem caracteres demais')

    return x
