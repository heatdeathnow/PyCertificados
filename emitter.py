from threading import Thread
from reportlab.pdfgen.canvas import Canvas
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from openpyxl import load_workbook
from time import time, sleep
from pdfrw import PdfReader
from textwrap import wrap
from reader import *
import neat
import var
from pandas import concat
from math import floor
from threading import active_count, Thread

template = PdfReader(var.template, decompress=False)
template_obj = pagexobj(template.pages[0])  # Carrega um objeto do PDF modelo.


# Método usado para emitir um certificado. Leva nome, CPF, CNPJ, matrícula, cliente, apólice e coberturas ou código.
def emit_singular(name, cpf, cnpj, matr, clie, apol, cobe='', cnv=''):
    with var.lock:
        var.progress += 1

    if cobe != '':
        text = f"Informamos que o segurado ativo pelo CNPJ: {neat.cnpj(cnpj)}, Apólice: {apol} " \
               f"Nome: {neat.name(name)}, CPF: {neat.cpf(cpf)}, Matrícula: {neat.matr(matr)}, contratado pelo " \
               f"cliente {clie}, consta ativo na apólice do seguro de vida em grupo com as coberturas: {cobe}, " \
               f"com vigência das 24:00h de {var.start_period} Até 24:00h de {var.end_period}."

    else:
        text = f"Informamos que o segurado ativo pelo CNPJ: {neat.cnpj(cnpj)}, Apólice: {apol} " \
               f"Nome: {neat.name(name)}, CPF: {neat.cpf(cpf)}, Matrícula: {neat.matr(matr)}, contratado pelo " \
               f"cliente {clie}, consta ativo na apólice do seguro de vida em grupo com as coberturas: {cnv}, " \
               f"com vigência das 24:00h de {var.start_period} Até 24:00h de {var.end_period}."

    canvas = Canvas(f'{var.output_dir}{neat.cpf(cpf)} - {neat.name(name)}.pdf')  # Objeto do texto a ser salvo.

    xobj_name = makerl(canvas, template_obj)  # Superposição objeto modelo com o objeto escritor por cima.
    canvas.doForm(xobj_name)

    lines = wrap(text, 80)  # Quebra o texto contínuo em linha com no máximo segundo parâmetro de caracteres.
    y = 620  # Altura inicial do texto no PDF
    x = 65  # Distância do texto à esquerda do PDF

    for line in lines:
        canvas.drawString(x, y, line)  # Escreve a linha por cima do modelo.
        y -= 15  # Espaçamento entre as linhas

    canvas.save()  # Função I/O-intensiva para salvar o arquivo da memória para o armazenamento do computador.


def emit_from_source():  # Função para emitir diversos certificados advindos de uma fonte de dados externa.
    start_time = time()  # Horário do começo da emissão.
    cnv = get_cnv(var.cnv_path)

    # Abre a planilha no modo leitura otimizada para obter o número de linhas e então fechá-la.
    row_count_time = time()
    workbook = load_workbook(filename=var.data_dir, read_only=True)
    sheet = workbook.worksheets[0]
    row_count = sheet.max_row - 1  # Desconta os cabeçários
    workbook.close()
    print(f'Tempo necessário para calcular que há {row_count} linhas na planilha: {(time() - row_count_time):.2f} segundos.')

    var.max_progress = row_count

    # Sabendo o número total de linhas, divide-se o trabalho de carregá-las na memória através de multiprocessamento.
    quotient = floor(var.max_progress / var.max_processes)  # Número de linhas que cada processo irá carregar na memória.
    remainder = var.max_progress % var.max_processes  # Número de linhas a mais que o último processo carregará na memória.
    processes = []

    for i in range(var.max_processes):
        if i == range(var.max_processes)[-1]:  # Se estiver na última iteração, dê a sobra de linhas para o último processo.
            processes.append(SubLoader(var.data_dir, i * quotient, quotient + remainder, i, var.shared_list, var.lock))
        
        elif i == 0:  # Ignorar a primeira linha (cabeçários) no caso do começo da planilha
            processes.append(SubLoader(var.data_dir, 1, quotient, i, var.shared_list, var.lock))

        else:  # Senão, dê apenas o quociente da divisão para esses processos que não são o último.
            processes.append(SubLoader(var.data_dir, i * quotient, quotient, i, var.shared_list, var.lock))

        processes[i].start()

    for i in range(var.max_processes):
        processes[i].join()  # Espera todos os processos carregarem suas seções de dados na memória para então continuar o programa.

    headers = get_headers(var.data_dir)  # Obtém a posição de cada coluna de dados importantes na planilha.

    df = concat(var.shared_list[:], ignore_index=True)  # Junta todas as partes num inteiro.
    for chunk in var.shared_list: del chunk  # Deleta os fragmentos de dados depois de serem utilizados.

    threads = []
    emit_time = time()  # Usado para calcular o tempo total e velocidade média do processo de emissão.

    # Usados para calcular velocidade marginal.
    marginal_time = time()
    marginal_cert = 0
    while var.progress < var.max_progress:   
        if headers['cobe'] != '' and active_count() < var.max_threads:
            threads.append(Thread(target=emit_singular, args=(df.iloc[var.progress, headers['name']],
                                                              df.iloc[var.progress, headers['cpf' ]],
                                                              df.iloc[var.progress, headers['cnpj']],
                                                              df.iloc[var.progress, headers['matr']],
                                                              df.iloc[var.progress, headers['clie']],
                                                              df.iloc[var.progress, headers['apol']],
                                                              df.iloc[var.progress, headers['cobe']],
                                                              '')))
            threads[-1].start()

        elif active_count() < var.max_threads:
            threads.append(Thread(target=emit_singular, args=(df.iloc[var.progress, headers['name']],
                                                              df.iloc[var.progress, headers['cpf' ]],
                                                              df.iloc[var.progress, headers['cnpj']],
                                                              df.iloc[var.progress, headers['matr']],
                                                              df.iloc[var.progress, headers['clie']],
                                                              df.iloc[var.progress, headers['apol']],
                                                              '',
                                                              cnv.loc[neat.cnv(df.iloc[var.progress, headers['cnv']])])))
            threads[-1].start()

        else:
            sleep(0.001)

        if marginal_cert != var.progress:
            print(f'Velocidade marginal: {(var.progress - marginal_cert) / (time() - marginal_time):06.2f} certificados por segundo. | Threads ativas: {active_count()}.')
            marginal_time = time()
            marginal_cert = var.progress

    for thread in threads:
        thread.join()

    print(f'Tempo levado para salvar {var.max_progress} arquivos PDF da memória para o disco: {(time() - emit_time) / 60:.2f} minutos')

    del df
    var.progress = 0
    var.emission_time = time() - start_time
    var.certificates_per_second = var.max_progress / var.emission_time
