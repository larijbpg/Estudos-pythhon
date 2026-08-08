
def soma_entre_numeros():
    # Criar um script em Python que leia dois numeros e tente mostrar a SOMA deles
    # n1= input('primeiro numero')
    # n2 =input('segundo numero')
    # x = n1 + n2

    # print('A soma vale', x)
    # print( type(x))
    # A soma vale 13 ----> CONCATENAÇÃO
    # <class 'str'>

                                                # Tipos primitivos

                                                # int() = numero inteiro -> 7, -4, 2550
                                                # float() = numero com casas decimais -> 7.0, -7.0, 0.0075
                                                # str() = texto - 'Olá', '7.5', ''= texto vazio
                                                # bool() = valores lógicos - True ou False


    n1 = int(input('primeiro numero:'))
    n2= int(input('segundo numero:'))
    x = n1 + n2
    print('A soma vale', x)
    print(type(x))

def operadores_aritmticos():
                                                        # OPERADORES ARITMÉTICOS
                                                        # ORDEM DE PRECEDÊNCIA
                                                            # 1º ()
                                                            # 2º 4**3/ pow(4,3)
                                                            # 3º * / // %
                                                            # 4º + -

    # 5 + 3 * 2 == 11
    # 3 * 5 + 4 ** 2 == 31
    # 3 * (5 + 4) ** 2 == 243

    n1 = int(input('Um valor:'))
    n2 = int(input('Outro valor:'))
    s = n1 + n2
    m = n1 * n2
    d = n1 / n2 # vai ser 3 casas apos a vírgula flutuante {:.3f}
    di = n1 // n2
    e = n1 ** n2

    print('A soma vale {}, \n produto vale {} \n e a divisão é {:.3f}'.format(s, m, d), end=' ')
    print('Divisão inteira {} e potencia {}'.format(di, e))

    # end='' no final juntou as linhas dos print's
    # para quebrar a linha -> /n -> nova linha

# Alinhamento
def alinhamento():
    nome = input('Qual é o seu nome?')

    print('Prazer em te conhecer {:=^20}!'.format(nome))
    print(f'Prazer em te conhecer {nome:=^20}!')


def raiz_quadrada():
    n = int(input('Escreva um numero:'))
    
    r = n ** (1/2)

    print(f'Seu numero é {n} e a raíz quadrada é {r:.2}')


# Programa que leia um numero inteiro e diga se ele é PAR OU ÍMPAR
def par_ou_impar():
    n = int(input('Escreva um numero inteiro:'))

    if n % 2 == 0 :
        print(f'O numero {n} é um numero par')
    else:
        print(f'{n} É um numero ímpar')

    # não usei " if n/2 is not float()" pq toda divisão com / vira float: 4/2 = 2.0 (True)


soma_entre_numeros()
#operadores_aritmticos()
#alinhamento()
#raiz_quadrada()
#par_ou_impar