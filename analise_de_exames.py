""" 
Crie uma função chamada tempo_restante_incubacao que:
Recebe um parâmetro chamado minutos_decorridos
O tempo total de incubação de uma amostra é sempre 45 minutos
A função deve devolver quantos minutos ainda faltam
"""

def tempo_restante_incubacao(minutos_decorridos):
    tempo_incubacao = 45

    return(tempo_incubacao - minutos_decorridos)


#=============================================================================================================================================================
"""
Crie uma função chamada verificar_resultado que: 
receba um parametro chamado valores_exames 
Se o valor_exame for maior que 100, deve devolver(return) a string 'positio'
caso contrario, deve devolver 'negativo
"""
def verificar_resultado(valor_exame):
    if valor_exame >= 100:
        return('positivo')
    else:
        return('negativo')


#============================================================================================================================================================
"""
Crie uma função chamada classificar_carga_viral que:
Recebe um parâmetro chamado valor
Se valor for maior que 1000, deve devolver 'alta'
Se valor for maior que 100 (mas até 1000), deve devolver 'média'
Caso contrário (100 ou menos), deve devolver 'baixa'
"""

def classificar_carga_viral(valor):
    if valor >= 1000:
        return('alta')
    if valor >= 100 and valor < 1000:
        return('média')
    else:
        return('baixa')



# ==========================================================================================================================================================

"""
Exercício - filtrar exames:
Crie uma função chamada exames_alterados(lista_valores) que recebe uma lista de valores de exames (números) e "retorna" uma nova lista contendo apenas os valores acima de 100 (considerados alterados)
Dica: você vai precisar de uma lista vazia dentro da função, um "for" percorrendo lista_valores, um "if" pra testar a condição, e no final um "return" dessa lista nova (não um print!).
"""

# Você deve criar uma função que receba uma lista de valores de exames e analise cada valor (for). 
# A função deve separar apenas os valores maiores que 100 (if) e armazená-los em uma nova lista (recebe). 
# Ao final, ela deve retornar essa nova lista contendo somente os exames alterados.


def exames_alterados(lista_valores):
    valores_acima = [] # tive que criar uma lista vazia pois preciso ter onde colocar esses valores durante o loop
    
    for valor in lista_valores: # já que quero avaliar valor por valor, crio um loop (for)
        if valor >= 100: # dou a condição para cada valor 
            valores_acima.append(valor) #adiciono numa lista nova apenas os valores que eu quero pegar 

    return (valores_acima) #peço para ele guardar essa lista nova para ser usada futuramente em  algum lugar


# ==========================================================================================================================================================

"""
Crie uma função chamada classificar_exames(lista_valores) que recebe uma lista de valores de carga viral 
e retorna uma lista de strings com a classificação de cada um, reaproveitando a lógica que você já fez em classificar_carga_viral:
    valor > 1000 → "alta"
    valor entre 100 e 1000 → "média"
    valor < 100 → "baixa"
Ou seja: em vez de rodar a função pra um valor só, ela vai processar a lista inteira e devolver uma lista de classificações, na mesma ordem dos valores de entrada."""

def classificar_exames(lista_valores):
    lista_classificacao = [] 
    for valor in lista_valores: # ele vai passar valor por valor nas 3 condições e adicionar ele na lista_classificacao
        if valor >= 1000:
            lista_classificacao.append('alta')
            
        if valor >= 100 and valor < 1000:
            lista_classificacao.append('média')
            
        if valor < 100:
            lista_classificacao.append('baixa')

    return lista_classificacao # colocar na identação do for e não do if pq assim que o return é executado, ele encerra o loop.

    
# Execução do Código (Chamdas) =======================================================================================================================

#tempo_restante_incubacao()
resultado = tempo_restante_incubacao(10) # chamei a função e preciso guardar o resultado em uma variavel
print(resultado)

#verificar_resultado()
#resultado = verificar_resultado(150)
#print(resultado)

#classificar_carga_viral()
#resultado1 = classificar_carga_viral(1500)
#resultado2 = classificar_carga_viral(50)
#print(resultado1)
#print(resultado2)

#exames_alterados()
#exames_pacientes = [50, 150, 99, 80, 110, 200]
#exames_alterados(exames_pacientes) #chamo a função que quero usar e dou os valores do parametro 
#print(exames_alterados(exames_pacientes))

#classificar_exames()
#valores_pacientes = [99, 123, 1080, 340, 550, 200, 1300, 1250]
#classificar_exames(valores_pacientes)
#print(classificar_exames(valores_pacientes))