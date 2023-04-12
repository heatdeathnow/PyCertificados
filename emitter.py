from reportlab.pdfgen.canvas import Canvas
from pdfrw import PdfReader
from pdfrw.buildxobj import pagexobj
from pdfrw.toreportlab import makerl
import textwrap
from reader import *
import threading
import time
import parser
import var

template = PdfReader(var.template, decompress=False)
template_obj = pagexobj(template.pages[0])


# Método que gera o texto com os dados do beneficiário sem a apólice.
def textgen_without_apolice(nome, cpf, cnpj, matr, cobe):
    return f"Informamos que o segurado ativo pelo CNPJ: {cnpj}, Nome: {nome}, CPF: {cpf}, Matrícula: {matr}, " \
           f"consta ativo na apólice de seguro de vida em grupo com as coberturas: {cobe}, com vigência " \
           f"das 24:00h de {var.start_period} Até 24:00h de {var.end_period}."


def textgen_with_apolice(nome, cpf, cnpj, apol, matr, cobe):
    return f"Informamos que o segurado ativo pelo CNPJ: {cnpj}, Nome: {nome}, CPF: {cpf}, Matrícula: {matr}, " \
           f"consta ativo na apólice {apol} de seguro de vida em grupo com as coberturas: {cobe}, com vigência " \
           f"das 24:00h de {var.start_period} Até 24:00h de {var.end_period}."


# Método usado para emitir um certificado. Leva nome, CPF, CNPJ, matrícula e coberturas.
def emit_singular(name, cpf, cnpj, matr, cobe, apol=None):
    var.progress += 1

    if apol is None:
        text = textgen_without_apolice(parser.name(name), parser.cpf(cpf), parser.cnpj(cnpj), parser.matr(matr), cobe)
    else:
        text = textgen_with_apolice(parser.name(name), parser.cpf(cpf), parser.cnpj(cnpj), apol, parser.matr(matr), cobe)

    canvas = Canvas(f'{var.output_dir}{var.progress} - {parser.name(name)}.pdf')  # Objeto do arquivo a ser salvo.

    xobj_name = makerl(canvas, template_obj)  # Superposição objeto modelo com o objeto escritor por cima.
    canvas.doForm(xobj_name)

    lines = textwrap.wrap(text, 80)  # Quebra o texto contínuo em linha com no máximo segundo parâmetro de caracteres.
    y = 620  # Altura inicial do texto no PDF
    x = 75  # Distância do texto à esquerda do PDF

    for line in lines:
        canvas.drawString(x, y, line)  # Escreve a linha por cima do modelo.
        y -= 15  # Espaçamento entre as linhas

    canvas.save()


def emit_from_source():
    start_time = time.time()
    df = load(var.data_dir)
    headers = get_headers(df)

    var.max_progress = len(df.index)

    if var.apolice:
        while var.progress < len(df.index):
            if threading.active_count() < var.max_threads:
                threading.Thread(target=emit_singular(df.loc[var.progress, headers['name']], df.loc[var.progress,
                headers['cpf']], df.loc[var.progress, headers['cnpj']], df.loc[var.progress, headers['matr']],
                                                      df.loc[var.progress, headers['cobe']], df.loc[var.progress,
                    headers['apol']]), daemon=False).start()

    else:
        while var.progress < len(df.index):
            if threading.active_count() < var.max_threads:
                threading.Thread(target=emit_singular(df.loc[var.progress, headers['name']], df.loc[var.progress,
                headers['cpf']], df.loc[var.progress, headers['cnpj']], df.loc[var.progress, headers['matr']],
                                                      df.loc[var.progress, headers['cobe']]), daemon=False).start()

    var.progress = 0
    var.emission_time = time.time() - start_time
    var.certificates_per_second = len(df.index) / var.emission_time
