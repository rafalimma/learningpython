#Operadores in (esta entre) e not in (não esta entre)
'''
Strings são interáveis
0 1 2 3 4 5
R a f a e l
-6-7-8-9-2-3
'''
nome = 'Rafael'
print(nome[0]) #retorna o índice ou posição do caracter na string
print(nome[-1])
print('a' in nome)
print('f' not in nome)
print(10 * '-')

nome = input('digite o nome: ')
encontrar = input('digite o que deseja encontrar: ')

if encontrar not in nome:
    print(f'não existe {encontrar} em {nome}')
else:
    print(f'{encontrar} está em {nome}')
