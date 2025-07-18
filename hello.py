#!/usr/bin/env python3.11
"""
Trecho de Docstring
Hello World Multi Linguas.

Dependendo da linha configurada no 
ambiente o programa exibe a mensagem correspondente.

Boa prática, usar até a coluna 79. 
Não é obrigatório. 

Como usar: 
    Tenha a variável LANG devidamente configurada.
    Ex.:
        export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py

É bom ter a descrição no próprio script.
Maior que 20 linhas, é melhor ter uma documentação. 


Estilo
PEP8

abaixo temos os Dunders (Double Under)
variáveis de convenção para apontar informações que são importantes;

"""
__version__ = "0.0.1"
__author__ = "Eulino Netto"
__license__ = "Unlicense"

# Este programa imprime Hello World

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"


print(msg)


