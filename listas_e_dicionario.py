
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


# Escreva um for que imprime só as notas maiores ou iguais a 6.
def numeros_maiores_ou_igual():
    
    notas = [8.5, 4.0, 6.2, 9.9, 3.5, 7.0]
    for nota in notas:
        if nota > 6 or nota == 6:
            print(f'Sua nota foi {nota}. Parabens! Você foi aprovado!')
        else:
            print(f'Sua nota foi {nota}. Que pena! Você não foi aprovado.')

# VARIÁVEL ACUMULADORA

def variavel_acumuladora():
    # Some todos os valores da lista usando um for (sem usar a função pronta sum() 
    # — o objetivo é praticar o raciocínio manual). 
    # Dica: crie uma variável total = 0 antes do loop(for).

    valores_exame = [120, 95, 180, 75, 200]
    total = 0

    for valor in valores_exame:
        total = total + valor
    print(total)

    # No jeito certo, o total começa em 0 e vai crescendo aos poucos, uma soma de cada vez, dentro do loop — é isso que se chama de "variável acumuladora". 
    # O for não serve pra repetir o print, serve pra repetir o passo de somar.
    # total = 0 → começa "zerado"
    # Primeira volta do loop: valor = 120 → total = 0 + 120 = 120
    # Segunda volta: valor = 95 → total = 120 + 95 = 215
    # Terceira volta: valor = 180 → total = 215 + 180 = 395
    # ... e assim por diante até passar por todos


#Imprima só o nome dos pacientes com febre igual a True

def pacientes_com_febre():

    pacientes = [
        {'nome': 'Ana', 'idade': 45, 'febre': True},
        {'nome': 'Bruno', 'idade': 30, 'febre': False},
        {'nome': 'Carla', 'idade': 60, 'febre': True},
    ]

    for paciente in pacientes:
        if paciente['febre'] == True:
            print(paciente['nome'])
    # se essa paciente atual tiver a parte de febre igual a True, printe o nome dessa paciente.



lista_de_amostras()
#lista_de_numeros()
#numeros_maiores_ou_igual()
#variavel_acumuladora()
#pacientes_com_febre()