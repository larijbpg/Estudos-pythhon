# Programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$ 7.00 por km acima do limite.
v = float(input('Qual a velocidade do carro?'))
# 1km - 7.00
# v - 80 -- m
# m = (v-80) * 7.00
if v>80 :
    m = (v-80) * 7.00
    print(emoji.emojize(f'Atenção:warning: \nVocê está acima do limite. \nVocê levou uma multa de {m:.2f}'))
else:
    print()