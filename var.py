from PySide6.QtWidgets import QFileDialog, QMessageBox, QApplication
from pdfrw.buildxobj import pagexobj, PdfDict
from reportlab.pdfgen.canvas import Canvas
from multiprocessing import cpu_count
from locale import setlocale, LC_ALL
from pdfrw import PdfReader
from yaml import safe_load
from os.path import exists
from datetime import date
from os import getcwd
from sys import argv


def critical_select_sheet(name: str) -> str | None:
    """
    Quando o programa falha em encontrar alguma planilha essencial que ele precisa para funcionar, ele exigirá que uma seja selecionada, ou terminará.
    """

    while True:
        warning = QMessageBox()
        warning.setWindowTitle('AVISO')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close)
        warning.setText(f'Arquivo contendo {name} não foi encontrado\n'
                        f'Clique em ok para selecioná-lo\n'
                        f'Ou clique em close para terminar o programa.')

        if warning.exec() == QMessageBox.StandardButton.Ok:
            file = QFileDialog.getOpenFileName()[0]

            if file[-4:].lower() in ('xlsx', '.xls', '.csv', 'xlsm'):
                return file.replace(work_directory, '')

        else:
            exit()


def critical_select_pdf() -> str | None:
    """
    Quando o programa falhar em encontrar o arquivo PDF modelo, ele exigirá que um seja selecionado ou terminará.
    """

    while True:
        warning = QMessageBox()
        warning.setWindowTitle('AVISO')
        warning.setIcon(QMessageBox.Icon.Warning)
        warning.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close)
        warning.setText(f'O PDF modelo não foi encontrado\n'
                        f'Clique em ok para selecioná-lo\n'
                        f'Ou clique em close para terminar o programa.')

        if warning.exec() == QMessageBox.StandardButton.Ok:
            file = QFileDialog.getOpenFileName()[0]

            if file[-4:].lower() == '.pdf':
                return file.replace(work_directory, '')

        else:
            exit()


def get_pdf_template() -> PdfDict:  # Abre o modelo PDF. (Isso tem que ser feito aqui para poder mudá-lo posteriormente nas configurações)
    """
    Carrega o modelo PDF na memória e o retorna, onde ele poderá ser utilizado para construir outros PDFs a partir de si e de um texto.
    """

    template = PdfReader(template_dir, decompress=False)
    return pagexobj(template.pages[0])  # Retorna um objeto do PDF modelo.


built_in_fonts = Canvas('').getAvailableFonts()  # Todas as fontes já embutidas no ReportLab
setlocale(LC_ALL, 'pt-BR.UTF-8')  # Localização é usado para formatar dinheiro quando há campo capital

app = QApplication(argv)  # É necessário que o QApplication seja inicializado antes das possíveis janelas de erro e QDialogs que o podem vir a usá-lo.

progress                = 0
max_progress            = 1
certificates_per_second = 0
emission_time           = 0
work_directory          = getcwd().replace('\\', '/') + '/'  # Diretório onde está sendo executado o programa para que ele possa salvar outros diretórios de maneira mais legível.
load_problem            = False  # Quando há algum problema de carregamento, o programa salva imediatamente após concluir um carregamento correto.
abort_emission          = False  # Usado para dar a opção de abortar a emissão quando a planilha está faltando colunas críticas.
headers = ''

# Essas variáveis são inicializadas aqui, mas seus valores são atribuídos no módulo main.
manager     = ''
shared_list = ''
lock        = ''

if not exists('dados/init.yaml'):
    open('dados/init.yaml', 'x').close()

with open('dados/init.yaml', 'r') as file:
    dic = safe_load(file.read())

# Código boilerplate para carregamento do arquivo init.yaml e possíveis erros que podem vir a acontecer.
try:
    max_threads = dic['max_threads']
except (KeyError, TypeError):
    print('Erro ao carregar número máximo de threads, assumindo valor padrão de 150.')
    max_threads = 150
    load_problem = True

try:
    max_processes = dic['max_processes']
except (KeyError, TypeError):
    print(f'Erro ao carregar número máximo de processos, assumindo valor padrão de {cpu_count()}.')
    max_processes = cpu_count()
    load_problem = True

try:
    target_threads = dic['target_threads']
except (KeyError, TypeError):
    print('Erro ao carregar número alvo de threads, assumindo valor padrão de 60.')
    target_threads = 60
    load_problem = True

try:
    data_dir = dic['data_dir']
except (KeyError, TypeError):
    print('Erro ao carregar diretório do arquivo padrão de emissão, pois não foi guardado. Deselecionando-o.')
    data_dir = ''
    load_problem = True
finally:
    if data_dir != '' and not exists(data_dir):
        print('Erro ao carregar diretório do arquivo de inicialização, pois ele não existe. Deselecionando-o.')
        data_dir = ''
        load_problem = True

try:
    output_dir = dic['output_dir']
except (KeyError, TypeError):
    print('Erro ao carregar diretório de saída, pois não foi guardado. Deselecionando-o.')
    output_dir = ''
    load_problem = True
finally:
    if output_dir != '' and not exists(output_dir):
        print('Erro ao carregar diretório de saída, pois ele não existe. Deselecionando-o.')
        output_dir = ''
        load_problem = True

try:
    start_period = dic['start_period']
except (KeyError, TypeError):
    print('Erro ao carregar data inicial de vigência, assumindo data padrão de 01/01/2023. ')
    start_period = date(2001, 1, 1)
    load_problem = True

try:
    end_period = dic['end_period']
except (KeyError, TypeError):
    print('Erro ao carregar data final de vigência, assumindo data padrão de 01/01/2023. ')
    end_period = date(2001, 1, 1)
    load_problem = True

try:
    cobertura_dir = dic['cobertura_dir']
except (KeyError, TypeError):
    print('Erro ao carregar arquivo com coberturas, pois não foi guardado. Começando processo para selecioná-lo.')
    load_problem = True
    cobertura_dir = critical_select_sheet('coberturas')
finally:
    if not exists(cobertura_dir):
        print('Erro ao carregar arquivo com coberturas, pois ele não existe. Começando processo para selecioná-lo.')
        load_problem = True
        cobertura_dir = critical_select_sheet('coberturas')

try:
    cnv_dir = dic['cnv_dir']
except (KeyError, TypeError):
    print('Erro ao carregar arquivo de códigos CNV, pois não foi guardado. Começando processo para selecioná-lo.')
    load_problem = True
    cnv_dir = critical_select_sheet('CNV')
finally:
    if not exists(cnv_dir):
        print('Erro ao carregar arquivo de códigos CNV, pois ele não existe. Começando processo para selecioná-lo.')
        load_problem = True
        cnv_dir = critical_select_sheet('CNV')

try:
    template_dir = dic['template_dir']
except (KeyError, TypeError):
    print('Erro ao carregar arquivo modelo PDF, pois não foi guardado. Começando processo para selecioná-lo.')
    load_problem = True
    template_dir = critical_select_pdf()
finally:
    if not exists(template_dir):
        print('Erro ao carregar arquivo modelo PDF, pois ele não existe. Começando processo para selecioná-lo.')
        load_problem = True
        template_dir = critical_select_pdf()

try:
    text_font = dic['text_font']
except (KeyError, TypeError):
    print('Erro ao carregar fonte do texto, assumindo valor padrão de Times-Roman')
    text_font = 'Times-Roman'
    load_problem = True

try:
    text_size = dic['text_size']
except (KeyError, TypeError):
    print('Erro ao carregar tamanho do texto, assumindo valor padrão de 12')
    text_size = 12
    load_problem = True

try:
    dist_left = dic['dist_left']
except (KeyError, TypeError):
    print('Erro ao carregar espaçamento à esquerda, assumindo valor padrão de 80.')
    dist_left = 80
    load_problem = True

try:
    text_height = dic['text_height']
except (KeyError, TypeError):
    print('Erro ao carregar altura do texto, assumindo valor padrão de 620.')
    text_height = 620
    load_problem = True

try:
    line_space = dic['line_space']
except (KeyError, TypeError):
    print('Erro ao carregar espaçamento entre as linhas, assumindo valor padrão de 15.')
    line_space = 15
    load_problem = True

try:
    max_chars = dic['max_chars']
except (KeyError, TypeError):
    print('Erro ao carregar número de caracteres antes de quebrar a linha, assumindo valor padrão de 85.')
    max_chars = 85
    load_problem = True

try:
    base_text = dic['base_text']
except (KeyError, TypeError):
    print('Erro ao carregar texto base padrão, continuando sem ele.')
    base_text = ''
    load_problem = True

try:
    name_keywords = dic['name_keywords']
except (KeyError, TypeError):
    print('Erro ao carregar palavras-chave para nome, assumindo valor padrão de "NOME".')
    name_keywords = ['NOME']
    load_problem = True

try:
    cpf_keywords = dic['cpf_keywords']
except (KeyError, TypeError):
    print('Erro ao carregar palavras-chave para CPF, assumindo valor padrão de "CPF".')
    cpf_keywords = ['CPF']
    load_problem = True

try:
    cnpj_keywords = dic['cnpj_keywords']
except (KeyError, TypeError):
    print('Erro ao carregar palavras-chave para CNPJ, assumindo valor padrão de "CNPJ".')
    cnpj_keywords = ['CNPJ']
    load_problem = True

try:
    matricula_keywords = dic['matricula_keywords']
except (KeyError, TypeError):
    print('Erro ao carregar palavras-chave para matrícula, assumindo valor padrão de "MATRICULA".')
    matricula_keywords = ['MATRICULA']
    load_problem = True

try:
    cliente_keywords = dic['cliente_keywords']
except (KeyError, TypeError):
    print('Erro ao carregar palavras-chave para cliente, assumindo valor padrão de "CLIENTE".')
    cliente_keywords = ['CLIENTE']
    load_problem = True

try:
    apolice_keywords = dic['apolice_keywords']
except (KeyError, TypeError):
    print('Erro ao carregar palavras-chave para apólice, assumindo valor padrão de "APOLICE".')
    apolice_keywords = ['APOLICE']
    load_problem = True

try:
    capital_keywords = dic['capital_keywords']
except (KeyError, TypeError):
    print('Erro ao carregar palavras-chave para capital, assumindo valor padrão de "CAPITAL".')
    capital_keywords = ['CAPITAL']
    load_problem = True

try:
    cobertura_keywords = dic['cobertura_keywords']
except (KeyError, TypeError):
    print('Erro ao carregar palavras-chave para cobertura, assumindo valor padrão de "COBERTURA".')
    cobertura_keywords = ['COBERTURA']
    load_problem = True

try:
    cnv_keywords = dic['cnv_keywords']
except (KeyError, TypeError):
    print('Erro ao carregar palavras-chave para CNV, assumindo valor padrão de "CNV".')
    cnv_keywords = ['CNV']
    load_problem = True

template_obj = get_pdf_template()
