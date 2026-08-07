"""Em Python, a palavra-chave def vem de "define" (definir). 
Ela serve para criar uma função, ou seja, para empacotar um bloco de código sob um nome específico para que você possa reutilizá-lo quantas vezes quiser 
sem precisar reescrever as mesmas linhas.

PQ USAR O DEF?
    Evita repetição de código (Reutilização): Escreveu uma lógica complexa de limpeza de texto uma vez? Empacote num def e use em dezenas de lugares.
    Organização e Leitura: Divide um problema gigante em pequenas funções com responsabilidades únicas (ex: uma função valida o CPF, outra formata o nome, outra salva no banco).
    Manutenção fácil: Se a regra de negócio mudar, você só precisa alterar o código dentro do def correspondente, em vez de alterar o arquivo inteiro.
"""
# ========================================================================================================================================================================================
# ESTRUTURA BÁSICA : 
# A função pode ter parametro ou não.

def nome_da_funcao(parametro1, parametro2):
    # Corpo da função (instruções com Tab/indentação)
    resultado = parametro1 + parametro2
    return resultado

# ===========================================================================================================================================================================================
# COM PARÂMETRO (as informações de entrada que a função precisa receber para trabalhar. Podem ser vazios se a função não precisar de dados externos.)

# A função é uma "fórmula" pronta. Ela não sabe quem são os pacientes até receber a lista(pacientes_uti/pediatria).
def filtrar_febre(lista_de_pacientes):
    com_febre = []
    for paciente in lista_de_pacientes:
        if paciente['temperatura'] > 37.8:
            com_febre.append(paciente['nome'])
    return com_febre

# Hoje você usa com a UTI:
pacientes_uti = [{"nome": "Ana", "temperatura": 38.5}]
print(filtrar_febre(pacientes_uti))

# Amanhã você usa com a Pediatria:
pacientes_pediatria = [{"nome": "Bruno", "temperatura": 36.5}]
print(filtrar_febre(pacientes_pediatria))

#===========================================================================================================================================================================================

# SEM PARÂMETRO

# Ela mesma cria os dados ou pega do input() do usuário diretamente
def solicitar_cadastro():
    nome = input("Digite o nome do paciente: ")
    idade = input("Digite a idade: ")
    print(f"Paciente {nome}, {idade} anos, cadastrado com sucesso!")

# Para rodar, você não precisa "mandar" nada para ela:
solicitar_cadastro()