"""
Formatação básica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere) (><^) (quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
= - faz o numero aparecer antes do 0
"""

variavel = 'abc'
print(f'{variavel}')
print(f'{variavel: >10}') #10 espaços pra esquerda 
print(f'{variavel: <10}') #10 espaços pra direita
print(f'{variavel: ^10}')
print(f'{1000.3455456474:+.1f}')