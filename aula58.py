"""
Imprecisão de ponto flutuante
Double-precision floating-point format IEEE 754
https://en.wikipedia.org/wiki/Double-precision_floating-point_format
https://docs.python.org/pt-br/3/tutorial/floatingpoint.html
"""
import decimal

n1 = decimal.Decimal('0.1')
n2 = 0.7

n3 = n1 + n2 #operações com n flutuantes tendem a ser imprecisas
print(n3)
#podemos corrigir isso:
print(f'{n3:.2f}')
print(round(n3, 2))