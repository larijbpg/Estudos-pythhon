# Verificação se um ano é bissexto

from datetime import date 

"""
Um ano é bissexto se é divisível por 4,
ECETO se for divisível por 100 (aí não é bissexto),
A NAO SER que tbm seja divisível por 400 (aí volta a ser bissexto)
"""


def analisador_ano_bissexto():

    ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual'))

    if ano == 0:
        ano = date.today().year #quero pegar o ano da data de hoje do meu computador e guardar na variavel ano
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é bissexto')
    else:
        print(f'O ano {ano} NÃO é bissexto')

analisador_ano_bissexto()