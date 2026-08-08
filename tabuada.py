# DESAFIO: faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
def tabuada_manual():
    n = int(input('Digite seu numero para a tabuada:'))

    a = 1 * n 
    b = 2 * n 
    c = 3 * n 
    d = 4 * n 
    e = 5 * n 
    f = 6 * n 
    g = 7 * n 
    h = 8 * n 
    i = 9 * n 
    j = 10 * n 

    print('-' * 12)
    print(' 1 x {:2} = {:2} \n 2 x {:2} = {:2} \n 3 x {:2} = {:2} \n 4 x {:2} = {:2} \n 5 x {:2} = {:2} \n ' \
    '6 x {:2} = {:2} \n 7 x {:2} = {:2} \n 8 x {:2} = {:2} \n 9 x {:2} = {:2} \n 10 x{:2} = {:2}'.format(n, a, n, b, n, c, n, d, n, e, n, f, n, g, n, h, n, i, n, j))
    # print('{} x {:2} = {}'. format(n, 1, n*1))
    # print('{} x {:2} = {}'. format(n, 2, n*2))
    # ..
    print('-' * 12)
    # quero aprender a criar uma sequencia que se faz sozinha, pois tenho padrões

def tabuada_com_loop():
    # DESAFIO: faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
    n = int(input('Digite seu numero:'))

    # Crio a lista de 1 a 10 -> vou ate 11 pq o Python lê até 1 numero antes
    tabuada = range(1,11)

    # O for anda por essa lista, numero por numero
    for numero_atual in tabuada:
        print(f'{numero_atual} x {n} = {numero_atual * n}')

    # f' avisa ao Python que tudo o que estiver dentro de {} deve ser substituido pelo valor real e o resto é tratado como texto comum
    # numero_atual é o numero que o for pegou da lista tabuada

#tabuada_manual()
tabuada_com_loop()