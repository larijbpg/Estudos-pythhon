# Verifica se três segmentos de reta podem formar um triangulo
"""
Regra matemática: cada um dos segmentos precisa ser menor que 
a soma do comprimento dos outros dois.
"""


def analisador_de_triangulos():
    print('-'*20)
    print('Analisador de Triângulos')
    print('-'*20)

    r1 = float(input('Primeiro segmento:'))
    r2 = float(input('Segundo segmento:'))
    r3 = float(input('Terceiro segmento:'))
    print(f'Os numeros são {r1}, {r2} e {r3}')

    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('Os segmentos acima podem formar um triângulo') #Só é verdadeiro se as 3 condições forem verdadeiras!
    else: 
        print('Os segmentos não podem formar um triângulo')

analisador_de_triangulos()