from numpy import trunc, float64, int64
from unidecode import unidecode
from locale import currency
from pandas import isna


def name(x) -> str:
    """
    Retorna o nome em CAIXA ALTA e sem acentos.
    """

    return unidecode(str(x).upper())


def capi(x) -> str:
    """
    Retorna o capital formatado para R$ XXX.XXX,XX
    """

    try:
        if isna(x) or x == 'ERRO' or x == '':
            x = 0.0

        # Isso só faz sentido assumindo que a localidade do arquivo Excel cujos dados foram extraídos está em pt-BR
        # Isso causará erros se isso não for verdadeiro.
        # todo Fazer isso de uma maneira mais independente
        elif isinstance(x, str):
            x = x.replace('.', '').replace('R', '').replace('$', '').strip()
            x = float(x.replace(',', '.'))

        elif isinstance(x, (float64, int64)):
            x = float(x)

    except ValueError:
        x = 0.0

    return currency(x, grouping=True)


def cpf(x) -> str:
    if isna(x):
        x = ''

    elif isinstance(x, (float64, int64, int, float)):
        x = str(int(trunc(x)))

    x = x.replace('.', '').replace('-', '').replace('/', '').replace('\\', '').strip()

    # Se tiver faltando números no CPF, adiciona zeros no começo.
    if len(x) < 11:
        x = '0' * (11 - len(x)) + x

    elif len(x) > 11:
        raise Exception(f'CPF "{x}" tem caracteres demais')

    # Formata e retorna o CPF.
    return x[:3] + '.' + x[3:6] + '.' + x[6:9] + '-' + x[9:]


def cnpj(x) -> str:
    if isna(x):
        x = ''

    elif isinstance(x, (float64, int64, int, float)):
        x = str(int(trunc(x)))

    x = x.replace('.', '').replace('-', '').replace('/', '').replace('\\', '').strip()

    # Se tiver faltando números no CNPJ, adiciona zeros no começo.
    if len(x) < 14:
        x = '0' * (14 - len(x)) + x

    elif len(x) > 14:
        raise Exception(f'CNPJ "{x}" tem caracteres demais')

    # Formata e retorna o CNPJ.
    return x[:2] + '.' + x[2:5] + '.' + x[5:8] + '/' + x[8:12] + '-' + x[12:]


def matr(x) -> str:
    if isna(x):
        x = ''

    elif isinstance(x, (float64, int64, int, float)):
        x = str(int(trunc(x)))

    if len(x) < 6:
        x = '0' * (6 - len(x)) + x  # Matrícula deve ter 6 caracteres.

    return x

def grupo(x) -> str:
    if isna(x):
        return 'GERENTES'

    elif isinstance(x, str):
        x = int(x.upper().replace('GRUPO', '').strip())
        x = str(x)  # Para se livrar de possíveis zeros na esquerda

    elif isinstance(x, (float64, int64, float, int)):
        x = str(int(trunc(x)))

    return x
