from csv import reader

progress                = 0
max_progress            = 1
certificates_per_second = 0
emission_time           = 0

# Essas variáveis são inicializadas aqui, mas seus valores são atribuídos no módulo main.
manager     = ''
shared_list = ''
lock        = ''

# Usados para fazer a troca dos valores na aba de configurações depois de clicar no botão de confirmar.
max_threads_tweak     = None
max_processes_tweak   = None
target_threads_tweak  = None
data_dir_tweak        = None
output_dir_tweak      = None
start_period_tweak    = None
end_period_tweak      = None
coberturas_path_tweak = None
cnv_path_tweak        = None
template_tweak        = None

with open('dados/configs', 'r') as file:
    configs = list(reader(file, delimiter=';'))

    max_threads     = int(configs[0][1])
    max_processes   = int(configs[1][1])
    target_threads  = int(configs[2][1])
    data_dir        = configs[3][1]
    output_dir      = configs[4][1]
    start_period    = configs[5][1]
    end_period      = configs[6][1]
    coberturas_path = configs[7][1]
    cnv_path        = configs[8][1]
    template        = configs[9][1]
