from numpy import trunc, float64, int64
from unidecode import unidecode
from pandas import isna


def name(x):
    return unidecode(str(x).upper())  # Remove acentos e transforma o texto em CAIXA ALTA.


def cpf(x):
    if isna(x):
        x = ''

    elif type(x) in (float64, int64, int):
        x = str(int(trunc(x)))

    x = x.replace('.', '').replace('-', '').replace('/', '')

    # Se tiver faltando números no CPF, adiciona zeros no começo.
    if len(x) < 11:
        x = '0' * (11 - len(x)) + x

    elif len(x) > 11:
        raise Exception(f'CPF "{x}" tem caracteres demais')

    # Formata e retorna o CPF.
    return x[:3] + '.' + x[3:6] + '.' + x[6:9] + '-' + x[9:]


def cnpj(x):
    if isna(x):
        x = ''

    elif type(x) in (float64, int64, int):
        x = str(int(trunc(x)))

    x = x.replace('.', '').replace('-', '').replace('/', '')

    # Se tiver faltando números no CNPJ, adiciona zeros no começo.
    if len(x) < 14:
        x = '0' * (14 - len(x)) + x

    elif len(x) <= 15:
        x = x.replace('0', '', 1)

    else:
        raise Exception(f'CNPJ "{x}" tem caracteres demais')

    # Formata e retorna o CNPJ.
    return x[:2] + '.' + x[2:5] + '.' + x[5:8] + '/' + x[8:12] + '-' + x[12:]


def matr(x):
    if isna(x):
        x = ''

    elif type(x) in (float64, int64, int):
        x = str(int(trunc(x)))

    if len(x) < 6:
        x = '0' * (6 - len(x)) + x  # Matrícula deve ter 6 caracteres.

    elif len(x) > 6:
        raise Exception(f'Matrícula "{x}" tem caracteres demais')

    return x


def cnv(x):
    if isna(x) or type(x) == str:
        return 'GERENTES'

    elif type(x) in (float64, int64, int):
        x = str(int(trunc(x)))

    if len(x) < 4:
        x = '0' * (4 - len(x)) + x

    elif len(x) > 4:
        raise Exception(f'CNV "{x}" tem caracteres demais')

    return x
