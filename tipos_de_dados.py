# tipos_de_dados.py
# Explorando tipos primitivos e conversão entre eles

def conversao_de_tipos():
    """Mostra como o input sempre vem como string, e como converter pra outros tipos."""
    n = input('Digite um valor: ')
    print(type(n))  # como estou apenas com o input, ele sempre vai ser um string. Pedi para ele me dar o tipo do que foi escrito.

    n = float(input('Digite um valor: '))
    print(n)  # ele vai transformar meu numero em numero decimal

    n = bool(input('Digite um valor: '))
    print(n)  # aparece verdadeiro pois tem um valor dentro, caso não tivesse nenhum, ele apareceria falso


def testando_metodos_de_string():
    """Explora métodos que só existem pra strings: isalpha(), isupper()."""
    n = input('Digite algo: ')
    print(n.isalpha())  # alfa -> é letra? "www" é letra -> True, "123" não é -> False

    n = input('Escreva algo')
    print(n)
    print(type(n))
    print(n.isupper())  # verifica se está tudo em maiúscula


# Escolha qual função rodar (descomente a que quiser testar):
conversao_de_tipos()
# testando_metodos_de_string()  -- só tirar a # se eu quiser testa-la