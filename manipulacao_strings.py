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

def gerar_iniciais(nome_paciente):

    palavras = nome_paciente.split()
    #não posso colocar o .title dps de .split pq o title funciona para colocar todas as letras maiusculas da string, se eu dou split antes, nao existe mais uma frase.
    print(palavras) 
    conectivos = ["da", "de", "do", "das", "dos", "e"]
    iniciais = "" #variavel com caixa de texto vazia

    for palavra in palavras:
        if palavra.lower() not in conectivos:
            iniciais += palavra[0].upper() + "." 
            # o operador de atribuição cumulativa += serve para ir colando o texto novo no texto ja guardado (seria -> iniciais = iniciais + palavra[0].upper() + ".")
            # na primeira volta do for ('carlos'), pega a primeira letra deixa maiuscula e coloca na frente o ponto "C." 
            # Na segunda volta, pega a primeira letra da segunda palavra 
    return iniciais 
   

    nome = ('   carlos eduardo da silva   ')
    resultado = gerar_iniciais(nome)
    print(resultado)

    """ 
    Objetivo: Praticar o uso correto de return e o tratamento de strings imutáveis.
    O Desafio:
    Crie uma função chamada gerar_iniciais que receba o nome completo de um paciente (mesmo com espaços extras nas pontas ou letras em caixa alta/baixa) 
    e retorne apenas as iniciais das palavras em maiúsculo, ignorando conectivos (da, de, do, das, dos, e).
    Entrada esperada: '   carlos eduardo da silva   '
    Saída esperada da função: 'C.E.S.'
    Dica: Lembre-se de usar .strip(), .split() e garantir que sua função use a palavra return no final!
    """

    """
    palavra = 'carlos'
    # print("A palavra inteira é:", palavra)
    # print("A primeira letra é:", palavra[0])
    # print("A primeira letra maiúscula é:", palavra[0].upper())
    # print("A primeira letra com ponto fica:", palavra[0].upper() + ".")
    """
# =======================================================================================================================================




manipulacao_print()
#manipulacao_de_nome()
#primeira_palavra()
#procurar_nome()