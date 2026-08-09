#Explorando emojis
def emojis():
    import emoji

    print(emoji.emojize('Olá mundo! :alien:', language='alias'))

    # sem a função .emojjize()
    texto = 'Python é :snake: '
    print(texto)

    # com a função .emojize()
    resultado = emoji.emojize(texto)
    print(resultado)

    print(emoji.demojize('Python é ❤'))

def tocar_musica():

    # Desafio: Faça um program em Python que abra e reproduza um arquivo em mp3
    # você precisa ter o arquivo no seu computador
    import pygame

    pygame.init()
    pygame.mixer.music.load('zayn_trampoline.mp3')
    pygame.mixer.music.play()

    input('Pressione ENTER para parar a musica:')
    pygame.mixer.music.stop()


emojis()
#tocar_musica()