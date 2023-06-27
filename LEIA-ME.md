### Módulos proprietários
Esse programa não utiliza módulos proprietários, porém foi feito utilizando o PyCreator, que é uma ferramenta proprietária. Por causa disso, deixo seu código aberto e disponível nesse repositório conforme a licença do PyCreator exige. A interface foi, então, feita usando PySide6, que é de código aberto, em vez do PyQt6, que é proprietário.

### Emissão de certificados

#### Singular
Esse programa permite a emissão de certificados para seguros através do preenchimento de campos no seção de emissão única. Campos que não estão sendo usados no texto não são obrigatórios de serem preenchidos (vide configurações). É possível escolher manualmente a cobertura da lista carregada pelo programa, mas também pode-se associar códigos numéricos às coberturas e selecioná-las dessa forma.

#### Múltiplos
Esse programa também permite a amissão de vários certificados de uma só vez. Isso é feito através da leitura dos dados de uma planilha. Se houver muitos beneficiários para emitir certificados, o programa usa multiprocessamento e _multithreading_. O multiprocessamento é usado para carregar os dados na memória de maneira mais efetiva, enquanto o _multithreading_ é usado para emitir mais de um certificado ao mesmo tempo, visto que o ato de gravar dados no disco é _I/O-Bound_.

### Configurações
O programa é altamente configurável: é possível trocar o PDF modelo; trocar as planilhas de coberturas e códigos de coberturas; editar o conteúdo do texto dos certificados e sua formatação; configurar as palavras-chave a serem procuradas na planilha; configurar o número de threads e processos permitidos, assim como o número de threads alvo.
