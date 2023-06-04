
import random

lista = []
count = 0
for count in range(16):
    n = random.randint(0, 50)
    if n in lista:
        continue
    lista.append(n)

lista.sort()
print(lista) #lista de numeros aleatorios diferentes

def busca(lista, item, comeco=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if comeco <= fim:
        m = (comeco + fim)//2 #mediana da lista
        if lista[m] == item:
            return f'O índice do item escolhido é {m}'
        if item < lista[m]:
            #m = (m//2)
            return busca(lista, item, comeco, m-1)
        else:
            return busca(lista, item, m+1, fim)
    return 'esse índice não existe na lista'

while True:
    item = input('Qual item você quer buscar na lista?')
    item = int(item)
    print(busca(lista, item))

