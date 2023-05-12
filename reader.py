from PySide6.QtWidgets import QMessageBox
from pandas import read_excel, read_csv
from multiprocessing import Process
from time import time
import var


# Função load usada exclusivamente para multiprocessamento. Em vez de retornar o valor, ele o salva numa variável multiprocessamento no módulo var.
class SubLoader(Process):
    def __init__(self, path, skiprows, nrows, i, mlist, lock, headers=False):
        super().__init__()
        self.path = path
        self.skiprows = skiprows
        self.nrows = nrows
        self.i = i
        self.list = mlist
        self.headers = headers
        self.lock = lock
        self.loadtime = time()

    def run(self):
        if self.headers:
            if self.path[-4:] == "xlsx" or self.path[-4:] == ".xls" or self.path[-4:] == "xlsm":
                with self.lock:
                    self.list[self.i] = read_excel(self.path, skiprows=self.skiprows, nrows=self.nrows)

            elif self.path[-4:] == ".csv":
                with self.lock:
                    self.list[self.i] = read_csv(self.path, skiprows=self.skiprows, nrows=self.nrows, sep=';')

        else:
            if self.path[-4:] == "xlsx" or self.path[-4:] == ".xls" or self.path[-4:] == "xlsm":
                with self.lock:
                    self.list[self.i] = read_excel(self.path, skiprows=self.skiprows, nrows=self.nrows, header=None)

            elif self.path[-4:] == ".csv":
                with self.lock:
                    self.list[self.i] = read_csv(self.path, skiprows=self.skiprows, nrows=self.nrows, sep=';', header=None)

        print(f'Tempo levado para o {self.i + 1}º processo carregar {len(self.list[self.i].index)} linhas na memória: {(time() - self.loadtime):.2f} segundos.')


# Função que distingue entre arquivos Excel e CSV, os lê e retorna um dataframe com seu conteúdo. Frequentemente usado para ler apenas parte do arquivo.
def load(path, headers=True, **kwargs):
    if headers:
        if path[-4:] == "xlsx" or path[-4:] == ".xls" or path[-4:] == "xlsm":
            return read_excel(path, **kwargs)

        elif path[-4:] == ".csv":
            return read_csv(path, sep=';', **kwargs)

    else:
        if path[-4:] == "xlsx" or path[-4:] == ".xls" or path[-4:] == "xlsm":
            return read_excel(path, header=None, **kwargs)

        elif path[-4:] == ".csv":
            return read_csv(path, sep=';', header=None, **kwargs)


# Lê todos os códigos de cobertura num arquivo externo e retorna a relação cifras-coberturas num dataframe (usado para a emissão de múltiplos certificados).
def get_cnv(path):
    df = load(path)
    df = df.set_index('CNV')
    df = df.squeeze()

    return df


# Lê um arquivo externo com todas as possibilidades de coberturas (usado para a emissão de certificados individuais).
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


# Função que olha todos os cabeçários da planilha e compara seus nomes com palavras-chaves. Usado para descobrir onde estão os dados que serão usados numa planilha desconhecida.
def get_headers(path):
    df = load(path, nrows=1)

    headers = {'name': '',
               'cpf' : '',
               'cnpj': '',
               'matr': '',
               'clie': '',
               'apol': '',
               'cobe': '',
               'cnv' : ''}

    # Depois que encontrar tal palavra-chave, ele não a substituirá se achar outra instância dela.
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
            headers['name'] = df.columns.get_loc(column)
            nome_found = True

        elif 'cpf' in column.lower().strip() and not cpf_found:
            headers['cpf'] = df.columns.get_loc(column)
            cpf_found = True

        elif 'cnpj' in column.lower().strip() and not cnpj_found:
            headers['cnpj'] = df.columns.get_loc(column)
            cnpj_found = True

        elif 'cliente' in column.lower().strip() and not clie_found:
            headers['clie'] = df.columns.get_loc(column)
            clie_found = True

        elif ('matricula' in column.lower().strip() or 'matrícula' in column.lower().strip()) and not matr_found:
            headers['matr'] = df.columns.get_loc(column)
            matr_found = True

        elif 'cobertura' in column.lower().strip() and not cobe_found:
            headers['cobe'] = df.columns.get_loc(column)
            cobe_found = True

        elif 'cnv' in column.lower().strip() and not cnv_found:
            headers['cnv'] = df.columns.get_loc(column)
            cnv_found = True

        elif ('apolice' in column.lower().strip() or 'apólice' in column.lower().strip()) and not apol_found:
            headers['apol'] = df.columns.get_loc(column)
            apol_found = True

    if headers['name'] == '':
        warning = QMessageBox()
        warning.setText('Campo "nome" não foi encontrado na planilha')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    if headers['cpf'] == '':
        warning = QMessageBox()
        warning.setText('Campo "CPF" não foi encontrado na planilha')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    if headers['cnpj'] == '':
        warning = QMessageBox()
        warning.setText('Campo "CNPJ" não foi encontrado na planilha')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    if headers['clie'] == '':
        warning = QMessageBox()
        warning.setText('Campo "cliente" não foi encontrado na planilha')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    if headers['matr'] == '':
        warning = QMessageBox()
        warning.setText('Campo "matricula" não foi encontrado na planilha')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    if headers['cobe'] == '' and headers['cnv'] == '':
        warning = QMessageBox()
        warning.setText('Pelo menos uma das colunas deve existir na planilha:\n'
                        '"CNV" ou "cobertura"')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    if headers['apol'] == '':
        warning = QMessageBox()
        warning.setText('Campo "apolice" não foi encontrado na planilha')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setWindowTitle('AVISO')
        warning.exec()

    return headers  # Retorna um dicionário contendo os índices das colunas que contém os dados que serão usados.


def save_configs():
    with open('dados/configs', 'w') as file:

        rows = [
            f'n_threads   ;{var.max_threads}\n',
            f'n_processes ;{var.max_processes}\n',
            f'n_target    ;{var.target_threads}\n',
            f'data_dir    ;{var.data_dir}\n',
            f'output_dir  ;{var.output_dir}\n',
            f'start_date  ;{var.start_period}\n',
            f'end_date    ;{var.end_period}\n',
            f'cobertura   ;{var.coberturas_path}\n',
            f'cnv         ;{var.cnv_path}\n',
            f'template    ;{var.template}',
        ]

        file.writelines(rows)
