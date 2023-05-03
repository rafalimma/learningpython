"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número inteiro: ')


if num.isdigit() and int(num) % 2 == 0:
    print('esse número é par')

elif num.isdigit() and int(num) % 2 != 0:
    print('seu numero é impar')

else:
    print('digite corretamente')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Que horas são? ')
dia = 11
tarde = 17
noite = 23

if hora.isdigit() and int(hora) <= dia:
    print('bom dia')
elif hora.isdigit() and int(hora) <= tarde and int(hora) > dia:
    print('boa tarde')
elif hora.isdigit() and int(hora) > tarde and int(hora) < noite:    
    print('boa noite')
else:
    print('digite corretamente')

#OOUUUU:
try:
    entrada = input('que horas são')
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')




"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome?')
lennome = len(nome)

curto = lennome <= 4
norm = lennome > 5 and lennome <= 6
grande = lennome > 6

if curto:
    print('seu nome é curto')
elif norm:
    print('seu nome é normal')
else:
    print('Seu nome é muito grande')


