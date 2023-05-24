# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Rafa')# aceita apenas 1 valor
s1.add(33)
print(s1)
s1.update(('Olá Mundo', 1, 2, 3, 4)) #quando vc passar ele vai iterar
#sobre aquele valor
print(s1)
#s1.clear()
#print(s1)

s1.discard('Olá Mundo')
print(s1)

print(50 * '_')

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2,3,4}
s3 = s1 & s2
s3 = s2 - s1 #retorna os unicos valores que estão no da esquerda
#não retorna os que estão na direita
s3 = s2 ^ s1 
print(s3)
