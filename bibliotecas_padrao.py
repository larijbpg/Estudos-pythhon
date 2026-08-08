# bibliotecas_padrao.py
# Explorando bibliotecas padrão do Python: math e random

import math
import random

"""math traz funções matemáticas prontas, como raiz quadrada e arredondamento."""
"""random gera números aleatórios de formas diferentes."""
"""Combina random + lógica condicional num mini-jogo."""

def usando_math():
    num = int(input('Digite um numero: '))
    raiz = math.sqrt(num)

    print(f'A raiz de {num} é igual a {raiz}')
    print(f'A raiz de {num} é igual a {raiz:.3f}')  # arredonda pra 3 casas decimais
    print(f'A raiz de {num} é igual a {math.ceil(raiz)}')   # arredonda pra cima
    print(f'A raiz de {num} é igual a {math.floor(raiz)}')  # arredonda pra baixo


def usando_random():
    num = random.random()  # número decimal aleatório entre 0 e 1
    print(num)

    num = random.randint(1, 10)  # número inteiro aleatório entre 1 e 10
    print(num)

# Programa que faça o computador pensar em um numero inteiro entre 0 e 5,
# peça para o usuario tentar descobrir qual foi o numero escolhido.
# o programa deverá escrever na tela se o usuário venceu ou perdeu.

def jogo_adivinhar_numero():
    n = random.randint(0,5)
    num = int(input("Qual numero inteiro vou escolher entre 0 e 5?"))

    if num==n :
        print(emoji.emojize (f'Incrível! Você acertou!:clapping_hands: O numero foi {n}!'))
    else:
        print(emoji.emojize(f'Que pena! Você errou :confused_face: \nO numero era {n}. Vamos tentar de novo?'))



# Escolha qual função rodar 
usando_math()
# usando_random()
# jogo_adivinhar_numero()