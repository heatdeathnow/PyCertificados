from PySide6.QtWidgets import QMessageBox
import pandas


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


def get_cnv(path):
    df = load(path)
    df = df.set_index('CNV')
    df = df.squeeze()

    return df


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
               'matr': '',
               'clie': '',
               'apol': '',
               'cobe': '',
               'cnv' : ''}

    nome_found = False
    cpf_found  = False
    cnpj_found = False
    matr_found = False
    clie_found = False
    apol_found = False
    cobe_found = False
    cnv_found  = False

    for column in df.columns:

        if ('nome' in column.lower().strip() or 'segurado' in column.lower().strip()) and not nome_found:
            headers['name'] = column
            nome_found = True

        elif 'cpf' in column.lower().strip() and not cpf_found:
            headers['cpf'] = column
            cpf_found = True

        elif 'cnpj' in column.lower().strip() and not cnpj_found:
            headers['cnpj'] = column
            cnpj_found = True

        elif 'cliente' in column.lower().strip() and not clie_found:
            headers['clie'] = column
            clie_found = True

        elif ('matricula' in column.lower().strip() or 'matrícula' in column.lower().strip()) and not matr_found:
            headers['matr'] = column
            matr_found = True

        elif 'cobertura' in column.lower().strip() and not cobe_found:
            headers['cobe'] = column
            cobe_found = True

        elif 'cnv' in column.lower().strip() and not cnv_found:
            headers['cnv'] = column
            cnv_found = True

        elif ('apolice' in column.lower().strip() or 'apólice' in column.lower().strip()) and not apol_found:
            headers['apol'] = column
            apol_found = True

    if not any(headers['name']):
        warning = QMessageBox()
        warning.setText('Campo "nome" não foi encontrado na planilha')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    if not any(headers['cpf']):
        warning = QMessageBox()
        warning.setText('Campo "CPF" não foi encontrado na planilha')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    if not any(headers['cnpj']):
        warning = QMessageBox()
        warning.setText('Campo "CNPJ" não foi encontrado na planilha')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    if not any(headers['clie']):
        warning = QMessageBox()
        warning.setText('Campo "cliente" não foi encontrado na planilha')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    if not any(headers['matr']):
        warning = QMessageBox()
        warning.setText('Campo "matricula" não foi encontrado na planilha')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    if not any(headers['cobe']) and not any(headers['cnv']):
        warning = QMessageBox()
        warning.setText('Pelo menos uma das colunas deve existir na planilha:\n'
                        '"CNV" ou "cobertura"')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    if not any(headers['apol']):
        warning = QMessageBox()
        warning.setText('Campo "apolice" não foi encontrado na planilha')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    return headers
