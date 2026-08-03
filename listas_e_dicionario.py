
def lista_de_amostras():
    amostras = [
        {'nome': 'Harry', 'data': '2026-08-03', 'resultado': 'negativo'},
        {'nome': 'Hermione', 'data': '2026-08-03', 'resultado': 'positivo'},
        {'nome': 'Rony', 'data': '2026-08-03', 'resultado': 'negativo'},
        {'nome': 'Luna', 'data': '2026-08-03', 'resultado': 'positivo'}
    ]
    for amostra in amostras:
        if amostra['resultado'] == 'positivo':
            print(amostra['nome'])


def lista_de_numeros():
    numeros = [2, 7, 10, 3, 15]
    for numero in numeros:
        if numero > 5:
            print('Os numeros maiores que 5 são:', numero)



lista_de_amostras()
#lista_de_numeros()