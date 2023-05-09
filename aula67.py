"""
argumentos nomeados e não nomeados em funções python
argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    #definição
    print(f'{x=} y={y}', '|','x + y + z = ', x + y + z) #funçoes em python por padrão retornam (none)


soma(1, 2, 3)
soma(y=2, z=3, x=1) #argumentos nomeados
soma(1, y=2, z=3) #quando tem um parametro nomeado os que vem depois
                  #tem que ser obrigatóriamente nomeados



