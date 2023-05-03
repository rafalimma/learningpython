'''
Alterando strings com while
'''
nome = 'Rafa'
indice = 0
no_nome = ''
while indice < len(nome): #acumula valores dentro da variavel vazia
    letra = nome[indice]
    no_nome += f'*{letra}'
    print('*')
    indice += 1

    
print(no_nome)
