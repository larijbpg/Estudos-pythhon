# Desafio: um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
n1 = input('Digite o nome do aluno:')
n2 = input('Digite o nome do aluno:')
n3 = input('Digite o nome do aluno:')
n4 = input('Digite o nome do aluno:')

lista_alunos = [n1, n2, n3, n4]
x = random. choice(lista_alunos)

print('O aluno sorteado para ajudar foi', x)

# Desafio: sortear a ordem de apresentação de trabalho dos alunos e mostre a ordem sorteada

y = random. sample(lista_alunos, k=len(lista_alunos))
print('A ordem da apresentação será:', y)