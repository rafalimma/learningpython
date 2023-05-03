frase = 'Oaaaa adadiuiui'

i = 0
qtdapareceu_mais_vezes = 0
letraapareceu_maisvezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == '':
        i += 1
        continue

    #contar a letra
    qtd_atual = frase.count(letra_atual)
    if qtdapareceu_mais_vezes < qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letraapareceu_maisvezes = letra_atual
    i += 1 #somou o i no valor antigo
    break

print(
    'A letra que apareceu mais vezes foi '
    f'"{letraapareceu_maisvezes}" que apareceu '
    f'{qtdapareceu_mais_vezes}x'
)
