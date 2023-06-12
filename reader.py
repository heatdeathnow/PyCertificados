from pandas import read_excel, read_csv
from yaml import safe_load, safe_dump
from multiprocessing import Process
from unidecode import unidecode
from time import time
import var


# Função load usada exclusivamente para multiprocessamento. Em vez de retornar o valor, ele salva-o numa variável multiprocessamento no módulo var.
class SubLoader(Process):
    def __init__(self, path, skiprows, nrows, i, mlist, lock):
        super().__init__()
        self.path = path
        self.skiprows = skiprows
        self.nrows = nrows
        self.i = i
        self.list = mlist
        self.lock = lock
        self.loadtime = time()

    def run(self):
        if self.path[-4:] == "xlsx" or self.path[-4:] == ".xls" or self.path[-4:] == "xlsm":
            with self.lock:
                self.list[self.i] = read_excel(self.path, skiprows=self.skiprows, nrows=self.nrows, header=None)

        elif self.path[-4:] == ".csv":
            with self.lock:
                self.list[self.i] = read_csv(self.path, skiprows=self.skiprows, nrows=self.nrows, sep=';', header=None)

        print(f'Tempo levado para o {self.i + 1}º processo carregar {len(self.list[self.i].index)} linhas na memória: {(time() - self.loadtime):.2f} segundos.')


# Função que distingue entre arquivos Excel e CSV, os lê e retorna um dataframe com o seu conteúdo. Frequentemente usado para ler apenas parte do arquivo.
def load(path, **kwargs):
    if path[-4:] == "xlsx" or path[-4:] == ".xls" or path[-4:] == "xlsm":
        return read_excel(path, **kwargs)

    elif path[-4:] == ".csv":
        return read_csv(path, sep=';', **kwargs)


# Lê todos os códigos de cobertura num arquivo externo e retorna a relação cifras-coberturas num dataframe (usado para a emissão de múltiplos certificados).
def get_cnv(path):
    df = load(path)
    df = df.set_index('CNV')
    df = df.squeeze()

    return df


def get_cnv_values(path):
    df = load(path)
    cnv = []
    from pandas import isna
    for i in range(len(df.index)):
        if not isna(df.iloc[i][1]):
            cnv.append(df.iloc[i][0])

    return cnv


# Lê um arquivo externo com todas as possibilidades de coberturas (usado para a emissão de certificados individuais).
def get_coberturas(path):
    df = load(path, header=None)
    df.columns = df.iloc[0]
    cobe = []

    try:
        for value in df.values:
            cobe.append(value[0])
    except IndexError:
        cobe = df.values

    return cobe


# Função que olha todos os cabeçários da planilha e compara os seus nomes com palavras-chave. Usado para descobrir onde estão os dados que serão usados numa planilha desconhecida.
def get_headers(path):
    df = load(path, nrows=1)

    headers = {'name': '',
               'cpf' : '',
               'cnpj': '',
               'matr': '',
               'clie': '',
               'apol': '',
               'capi': '',
               'cobe': '',
               'cnv' : ''}

    # Depois que encontrar tal palavra-chave, ele não a substituirá se achar outra instância dela.
    nome_found = False
    cpf_found  = False
    cnpj_found = False
    matr_found = False
    clie_found = False
    apol_found = False
    capi_found = False
    cobe_found = False
    cnv_found  = False

    for column in df.columns:

        if any(key in unidecode(column.lower().strip()) for key in var.name_keywords) and not nome_found:  # Se qualquer chave na lista de chaves é contida nessa coluna, então é a coluna certa.
            headers['name'] = df.columns.get_loc(column)
            nome_found = True

        elif any(key in unidecode(column.lower().strip()) for key in var.cpf_keywords) and not cpf_found:  # Em todas essas iterações, lê se o nome da coluna em minísculo e se acentos.
            headers['cpf'] = df.columns.get_loc(column)
            cpf_found = True

        elif any(key in unidecode(column.lower().strip()) for key in var.cnpj_keywords) and not cnpj_found:
            headers['cnpj'] = df.columns.get_loc(column)
            cnpj_found = True

        elif any(key in unidecode(column.lower().strip()) for key in var.cliente_keywords) and not clie_found:
            headers['clie'] = df.columns.get_loc(column)
            clie_found = True

        elif any(key in unidecode(column.lower().strip()) for key in var.matricula_keywords) and not matr_found:
            headers['matr'] = df.columns.get_loc(column)
            matr_found = True

        elif any(key in unidecode(column.lower().strip()) for key in var.cobertura_keywords) and not cobe_found:
            headers['cobe'] = df.columns.get_loc(column)
            cobe_found = True

        elif any(key in unidecode(column.lower().strip()) for key in var.capital_keywords) and not capi_found:
            headers['capi'] = df.columns.get_loc(column)
            capi_found = True

        elif any(key in unidecode(column.lower().strip()) for key in var.cnv_keywords) and not cnv_found:
            headers['cnv'] = df.columns.get_loc(column)
            cnv_found = True

        elif any(key in unidecode(column.lower().strip()) for key in var.apolice_keywords) and not apol_found:
            headers['apol'] = df.columns.get_loc(column)
            apol_found = True

    return headers  # Retorna um dicionário contendo os índices das colunas que contém os dados que serão usados.


def emergency_save():  # Essa função salva todos os valores atuais
    with open('dados/init.yaml', 'w') as file:
        safe_dump({
            'max_threads'        :        var.max_threads,
            'max_processes'      :      var.max_processes,
            'target_threads'     :     var.target_threads,
            'data_dir'           :           var.data_dir,
            'output_dir'         :         var.output_dir,
            'start_period'       :       var.start_period,
            'end_period'         :         var.end_period,
            'cobertura_dir'      :      var.cobertura_dir,
            'cnv_dir'            :            var.cnv_dir,
            'template_dir'       :       var.template_dir,
            'dist_left'          :          var.dist_left,
            'text_height'        :        var.text_height,
            'line_space'         :         var.line_space,
            'max_chars'          :          var.max_chars,
            'base_text'          :          var.base_text,
            'name_keywords'      :      var.name_keywords,
            'cpf_keywords'       :       var.cpf_keywords,
            'cnpj_keywords'      :      var.cnpj_keywords,
            'matricula_keywords' : var.matricula_keywords,
            'cliente_keywords'   :   var.cliente_keywords,
            'apolice_keywords'   :   var.apolice_keywords,
            'capital_keywords'   :   var.capital_keywords,
            'cobertura_keywords' : var.cobertura_keywords,
            'cnv_keywords'       :       var.cnv_keywords,
        }, file)


def push(name, value):  # Essa função salva um valor específico.
    with open('dados/init.yaml', 'r') as file:
        dic = safe_load(file.read())

    dic[name] = value

    with open('dados/init.yaml', 'w') as file:
        safe_dump(dic, file)


if var.load_problem : emergency_save()  # Depois que os dois módulos estiverem carregados, se houve erro de carregamento, salve os novos valores.
