'''
dict comprehenshin só que de chave e valor
novo_dict = {chave: valor for item in original if condicao}
'''

lances = [100, 200, 500, 600, 300]
so_validados = {l: "Aprovado" for l in lances if l > 250}
lances_validos = {l: ("Aprovado" if l > 250 else "Reprovado") for l in lances}
print('lances validos ou reprovados')
print(lances_validos)
print('lances validos')
print(so_validados)

# Como criaria um dicionário onde o número é a chave e o dobro dele é o valor?

nums = [5, 7, 8, 9, 8, 20]

dobros = {n: n*2 for n in nums}
print(dobros)