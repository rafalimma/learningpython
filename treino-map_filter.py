'''
map. Neste exemplo,
vamos criar uma função que recebe uma lista de números e retorna uma nova
lista com os números elevados ao quadrado.
'''


def quadrado(iteravel):
    return iteravel * iteravel


numbers = [1, 2, 3, 4, 5]

numeros_aoquadrado = list(map(#map ja passa cada valor que esta dentro do iteravel
    quadrado,#função primeiro, iterável depois
    numbers
))
print(numeros_aoquadrado)


'''
Aqui está um exercício um pouco mais complexo que utiliza tanto a função
map quanto a função filter. Neste exemplo,
vamos criar uma função que recebe uma lista de números
e retorna uma lista contendo apenas os números pares elevados ao cubo.
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def ao_cubo(j):
    return j * j * j

def so_pares(i):
    if i % 2 == 0:
        return i

pares = list(filter(
    so_pares,
    numbers
))

pares_aocubo = list(map(
    ao_cubo,
    pares
))

print(f'esses são os pares ao cubo {pares_aocubo}')
