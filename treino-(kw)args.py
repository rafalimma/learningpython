'''
Aqui está um exercício que envolve a criação de uma função que utiliza
*args para calcular a média de uma lista variável de números:

Exercício: Cálculo da Média com *args
O objetivo deste exercício é criar uma função que calcule
a média de uma lista variável de números passados como argumentos usando *args.
'''

def calcular_media(*args, **kwargs):
    soma = sum(args, kwargs)
    media_t = soma/len(args)
    return f'A média das notas é {media_t}'

'''
numeros = []
while len(numeros) <= 6:
    numero = int(input('Digite sua média: '))
    numeros.append(numero)
'''


media = calcular_media(1, 3, 4, 5, 6, key=6)
print(media)
