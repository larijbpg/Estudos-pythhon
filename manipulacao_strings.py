# formas de formatar texto em Python

def manipulacao_print():
    n1 = int(input('primeiro numero:'))
    n2= int(input('segundo numero:'))
    x = n1 + n2
    # print('A soma entre', n1, 'e', n2, 'vale', x), existe uma sintaxe nova:

    print('a soma entre {} e {} vale {}'.format(n1, n2, x))
    print(f'A soma entre {n1} e {n2} vale {x}')

# Fatiamento de string
def manipulacao_de_nome():

    frase = 'Curso em Video Python'
    print(frase)
    print(frase[3])
    print(frase[3:13])
    print(frase[:13])
    print(frase[1:15:2])

    # se eu quiser escrever um texto grande e que ele apareça inteiro, é só usar 3 aspas:
    # print("""" kbskffshvhjbkh
    # .csd.nlh.hidnsdfksf
    # sdldslfjlgkjdljld """")

    print(len(frase))
    print(frase.count('o'))
    print(frase.upper().count('O'))
    print(frase.replace('Python', 'Android'))

    # string é imutável

    print('Curso' in frase)
    print(frase.find('video'))
    print(frase.lower().find('video'))
    print(frase.split())

# Programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"

def primeira_palavra():
    cidade = input('Digite o nome da sua cidade:')
    print(cidade)

    palavra = cidade.split()
    if palavra[0] == 'santo':
        print('A primeira palavra é santo')
    else:
        print('A primeira palavra NÃO é santo')

    print('santo' in cidade)

    print(cidade.find('santo'))


# Pprograma que leia o nome de uma pessoa e diga se ela tem silva no nome

def procurar_nome():
    nome = str(input('Digite seu nome completo:'))
    print (nome)

    if 'silva' in nome.lower():
        print('Você tem silva no nome')
    else:
        print('Você não tem silva no nome')

    # ====================================================================================

    # outra forma
    print(f'Seu nome tem Silva? {'silva' in nome.lower()}')
    # in não é um método é um operador


manipulacao_print()
#manipulacao_de_nome()
#primeira_palavra()
#procurar_nome()