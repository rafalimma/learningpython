'''
Repetiçoes
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito = quando um código não tem fim
'''
contador = 0
while contador <= 100:
    contador += 1

    if contador == 6:
        print('não vou mostrra os 6')
        continue #ele não printa o 6 e continua o laço
    if contador >= 10 and contador <= 27:
        print('dada')
        continue
    print(contador)
    if contador == 60:
        break
print('acabou')