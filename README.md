### Coisas a fazer e a estudar

#### QtDesigner
Eu estive usando o QtCreator para fazer a interface do programa, pois estive sob a impressão que é apenas ele que se pode usar para fazer interfaces de PySide6. Mas se pode usar o QtDesigner para criar arquivos .ui - eu estou assumindo que esses arquivos .ui podem ser traduzidos para várias linguagens diferentes como C/C++ ou Python usando seus respectivos módulos. Esse programa parecce ter mais funcionalidades, então eu devo começar a usá-lo agora e traduzir os arquivos .ui para .py através do comando `PySide6-uic`.

#### Signals & Slots
Com meu conhecimento rudimentar de PySide6 e PyQt6, eu fiz o código da interface de maneira questionável. Eu pretendo aprender a criar Slots e Signals da maneira correta e os conectar da forma como foram feitos para serem.

#### Decoradores
O código está infestado de comandos `print()` e variáveis que só servem para calcular o tempo de processamento de alguns processos. Isso seria muito melhor implementado se fosse feito através de decoradores, com melhor reutilização de código.

#### Aba de configurações
Boa parte do código ainda está _hardcoded_. Há de se criar uma terceira aba, de configurações, e fazer com que tudo que está _hardcoded_ pode ser variável e modificável facilmente através dali.
