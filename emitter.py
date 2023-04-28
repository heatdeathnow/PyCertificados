from reportlab.pdfgen.canvas import Canvas
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from time import time
from pdfrw import PdfReader
from textwrap import wrap
from reader import *
import parser
import var

template = PdfReader(var.template, decompress=False)
template_obj = pagexobj(template.pages[0])


# Método usado para emitir um certificado. Leva nome, CPF, CNPJ, matrícula e coberturas.
def emit_singular(name, cpf, cnpj, matr, clie, apol, cobe='', cnv=''):
    var.progress += 1

    if cobe != '':
        text = f"Informamos que o segurado ativo pelo CNPJ: {parser.cnpj(cnpj)}, Apólice: {apol} " \
               f"Nome: {parser.name(name)}, CPF: {parser.cpf(cpf)}, Matrícula: {parser.matr(matr)}, contratado pelo " \
               f"cliente {clie}, consta ativo na apólice do seguro de vida em grupo com as coberturas: {cobe}, " \
               f"com vigência das 24:00h de {var.start_period} Até 24:00h de {var.end_period}."

    else:
        text = f"Informamos que o segurado ativo pelo CNPJ: {parser.cnpj(cnpj)}, Apólice: {apol} " \
               f"Nome: {parser.name(name)}, CPF: {parser.cpf(cpf)}, Matrícula: {parser.matr(matr)}, contratado pelo " \
               f"cliente {clie}, consta ativo na apólice do seguro de vida em grupo com as coberturas: {cnv}, " \
               f"com vigência das 24:00h de {var.start_period} Até 24:00h de {var.end_period}."

    canvas = Canvas(f'{var.output_dir}{parser.cpf(cpf)} - {parser.name(name)}.pdf')  # Objeto do arquivo a ser salvo.

    xobj_name = makerl(canvas, template_obj)  # Superposição objeto modelo com o objeto escritor por cima.
    canvas.doForm(xobj_name)

    lines = wrap(text, 80)  # Quebra o texto contínuo em linha com no máximo segundo parâmetro de caracteres.
    y = 620  # Altura inicial do texto no PDF
    x = 65  # Distância do texto à esquerda do PDF

    for line in lines:
        canvas.drawString(x, y, line)  # Escreve a linha por cima do modelo.
        y -= 15  # Espaçamento entre as linhas

    canvas.save()


def emit_from_source():
    start_time = time()

    headers = get_headers(load(var.data_dir, 0, 1))
    headers_load_time = time() - start_time
    print(f'Tempo de carregamento de headers: {headers_load_time / 60} minutos')
    
    cnv = get_cnv(var.cnv_path)
    var.max_progress = 0

    i = 0
    while True:
        
        data_chunk_load_start = time()
        data_chunk = load(var.data_dir, i * var.chunk_size)
        data_chunk_load_time = time() - data_chunk_load_start
        print(f'\nTempo de carregamento de {i + 1}º datachunk: {data_chunk_load_time / 60} minutos')

        var.max_progress += len(data_chunk.index)

        j = 0
        while j < len(data_chunk.index):
            if headers['cobe'] != '':
                emit_singular(data_chunk.iloc[j, headers['name']],
                              data_chunk.iloc[j, headers['cpf' ]],
                              data_chunk.iloc[j, headers['cnpj']],
                              data_chunk.iloc[j, headers['matr']],
                              data_chunk.iloc[j, headers['clie']],
                              data_chunk.iloc[j, headers['apol']],
                              data_chunk.iloc[j, headers['cobe']],
                              '')

            else:
                emit_singular(data_chunk.iloc[j, headers['name']],
                              data_chunk.iloc[j, headers['cpf' ]],
                              data_chunk.iloc[j, headers['cnpj']],
                              data_chunk.iloc[j, headers['matr']],
                              data_chunk.iloc[j, headers['clie']],
                              data_chunk.iloc[j, headers['apol']],
                              '',
                              cnv.loc[parser.cnv(data_chunk.iloc[j, headers['cnv']])])

            j += 1
            print(f'Progresso: {var.progress} / {var.max_progress} | minuto {(time() - start_time) / 60}')

        if len(data_chunk.index) < var.chunk_size:
            break
        i += 1

        del data_chunk

    var.progress = 0
    var.emission_time = time() - start_time
    var.certificates_per_second = var.max_progress / var.emission_time
