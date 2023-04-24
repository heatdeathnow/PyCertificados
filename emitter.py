from reportlab.pdfgen.canvas import Canvas
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
from pdfrw import PdfReader
from textwrap import wrap
from reader import *
import threading
import parser
import time
import var

template = PdfReader(var.template, decompress=False)
template_obj = pagexobj(template.pages[0])


# Método usado para emitir um certificado. Leva nome, CPF, CNPJ, matrícula e coberturas.
def emit_singular(name, cpf, cnpj, clie, matr, cobe, apol):
    var.progress += 1

    text = f"Informamos que o segurado ativo pelo CNPJ: {parser.cnpj(cnpj)}, Apólice: {apol} " \
           f"Nome: {parser.name(name)}, CPF: {parser.cpf(cpf)}, Matrícula: {parser.matr(matr)}, contratado pelo " \
           f"cliente {clie}, consta ativo na apólice do seguro de vida em grupo com as coberturas: {cobe}, " \
           f"com vigência das 24:00h de {var.start_period} Até 24:00h de {var.end_period}."

    canvas = Canvas(f'{var.output_dir}{var.progress} - {parser.name(name)}.pdf')  # Objeto do arquivo a ser salvo.

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
    start_time = time.time()
    df = load(var.data_dir)
    headers = get_headers(df)
    var.max_progress = len(df.index)

    threads = []

    while var.progress < var.max_progress:
        if threading.active_count() < var.max_threads:
            threads.append(threading.Thread(target=emit_singular, args=(df.loc[var.progress, headers['name']],
                                                                        df.loc[var.progress, headers['cpf' ]],
                                                                        df.loc[var.progress, headers['cnpj']],
                                                                        df.loc[var.progress, headers['clie']],
                                                                        df.loc[var.progress, headers['matr']],
                                                                        df.loc[var.progress, headers['cobe']],
                                                                        df.loc[var.progress, headers['apol']]),
                                            daemon=False))

            threads[var.progress].start()

    var.progress = 0
    var.emission_time = time.time() - start_time
    var.certificates_per_second = len(df.index) / var.emission_time
