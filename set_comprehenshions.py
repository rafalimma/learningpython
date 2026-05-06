'''
set comprehenshion 
set é um conjunto em python
set não permite elementos duplicados e não garante ordem
'''
# novo set = {expresão for item in iteravel if consição}

# utilidade : quer extrair valores únicos de uma lista bagunçada ou processar dados
# ignorando repetições

categorias_sujas = ["eletronicos", "móveis", "eletronicos", "joias", "móveis", "joias"]

categorias_limpas = {c.upper() for c in categorias_sujas}
# aqui não se repetem mais
print(categorias_limpas)

#usando if e else no set

lances = [500, 300, 400, 750, 900]
reumo = {("alto" if l > 500 else "baixo") for l in lances}
# se ja existir aquele valor no set ele não coloca dnv
print(reumo)

#exerciio
# Você recebeu uma lista de nomes de cidades de onde vêm os lances:
cidades = ["Curitiba", "São Paulo", "curitiba", "SÃO PAULO", "Rio de Janeiro", "Curitiba"]

#Crie um Set Comprehension que transforme todos os nomes para letras minúsculas e remova as duplicadas.
cidades_minusculas = {cidade.lower() for cidade in cidades}
print(cidades_minusculas)