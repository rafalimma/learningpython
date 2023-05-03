"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""

v1 = 'a'
v2 = 'a'

print(id(v1))
print(id(v2))

condicao = False
passou_no_if = None

if condicao:
    print('Fça algo')
else:
    print('n faça')
    
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

