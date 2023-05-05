from time import time
from multiprocessing import cpu_count

# Essas variáveis são inicializadas aqui, mas seus valores são atribuídos no módulo main.
manager = ''
shared_list = ''
lock = ''
data_dir = ''

max_processes = cpu_count()
max_threads = 50
progress = 0
max_progress = 1
output_dir = ''
start_period = '01/01/2023'
end_period = '01/01/2023'
runtime = time()  # Horário em que o programa foi iniciado.
emission_time = 0
certificates_per_second = 0
coberturas_path = 'dados/coberturas.xlsx'
template = 'dados/modelo.pdf'
cnv_path = 'dados/cnv.xlsx'
