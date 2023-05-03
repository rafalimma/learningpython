#desempacotamento em chamadas
#de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 1,2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'

#a, *_, ap, c  = lista
#print(a, c)

for nome in lista:
    print(nome, end=' ')

print(*lista)