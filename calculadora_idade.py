# Desafio 2: Criar um script em Python que leia o dia, mes e ano de uma pessoa e mostre uma mensagem com a data formatada

dia = input('Qual é o dia do seu aniversário?')
mes = input('Qual é o mes do seu aniversário?')
ano = int(input('Qual é o ano do seu aniversário?')) # transformar str em numero inteiro para depois poder fazer o cálculo
x = 2026 - ano

print('Você nasceu no dia', dia, 'de', mes, 'de', ano, '. Você tem', x, 'anos, correto?')