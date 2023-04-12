import pandas
import var


def load(path, headers=True):

    if headers:
        if path[-4:] == "xlsx" or path[-4:] == ".xls" or path[-4:] == "xlsm":
            return pandas.read_excel(path)

        elif path[-4:] == ".csv":

            return pandas.read_csv(path, sep=';')

    else:
        if path[-4:] == "xlsx" or path[-4:] == ".xls" or path[-4:] == "xlsm":
            return pandas.read_excel(path, header=None)

        elif path[-4:] == ".csv":

            return pandas.read_csv(path, sep=';', header=None)


def get_coberturas(path):
    df = load(path, False)
    df.columns = df.iloc[0]
    cobe = []

    try:
        for value in df.values:
            cobe.append(value[0])
    except IndexError:
        cobe = df.values

    return cobe


def get_headers(df):
    headers = {'name': '',
               'cpf' : '',
               'cnpj': '',
               'apol': None,
               'matr': '',
               'cobe': ''}

    for column in df.columns:

        if 'nome' in column.lower() or 'segurado' in column.lower():
            headers['name'] = column

        elif 'cpf' in column.lower():
            headers['cpf'] = column

        elif 'cnpj' in column.lower():
            headers['cnpj'] = column

        elif 'matricula' in column.lower() or 'matrícula' in column.lower():
            headers['matr'] = column

        elif 'cobertura' in column.lower():
            headers['cobe'] = column

        elif var.apolice and ('apolice' in column.lower() or 'apólice' in column.lower()):
            headers['apol'] = column

    if not any(headers['name']):
        raise Exception('Não foi possível encontrar o campo "nome" na planilha.')

    if not any(headers['cpf']):
        raise Exception('Não foi possível encontrar o campo "cpf" na planilha.')

    if not any(headers['cnpj']):
        raise Exception('Não foi possível encontrar o campo "cnpj" na planilha.')

    if not any(headers['matr']):
        raise Exception('Não foi possível encontrar o campo "matricula" na planilha.')

    if not any(headers['cobe']):
        raise Exception('Não foi possível encontrar o campo "cobertura" na planilha.')

    if var.apolice and not any(headers['apol']):
        raise Exception('Não foi possível encontrar o campo "apolice" na planilha.')

    return headers
