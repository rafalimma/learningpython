#formatação básica de strings

v = 'Rafa'

print(f'{v: >10}') #10 espações a direita
print(f'{v: <4} dada ') #4 espações a esquerda
print(f'{v: ^5}')
print(f'{1213.45453:+.2f}') #sempre tem q ter o f strings

print(50 * '-')
#id

nome = 'rafa'
print(id(nome))
print(50 * '-')

#while dentor de while

linhas_qtd = 5
colums_qtd = 5
linhas = 1
while linhas <= linhas_qtd:
    coluna = 1
    while coluna <= colums_qtd:
        print(f'{linhas}, {coluna}')
        coluna += 1
    linhas += 1

print(50 *'-')

#palavra secreta game

palavra_secrata = 'game'
letras_acertadas = ''


while True:
    letra_digitada = input('Digite uma letra')
    if len(letra_digitada) > 1:
        print('digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secrata:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secrata:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('palavra formada:', palavra_formada)

    if palavra_formada == palavra_secrata:
        print('parabéns')