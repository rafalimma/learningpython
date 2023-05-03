'''
interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF012245)

'''

nome = 'Rafa'
preco = 100.0000
variavel = '%s, o preco é %f' % (nome, preco)

print(variavel)
print(10 * '-')
#hexadecimal
print('O Hexadecimal de %d é %04x' % (15, 15))
