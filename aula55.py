"""
tipo tupla = uma lista imutável
"""

#nomes = ['Maria', 'Helena', 'Luiz']
#lista sem conchetes vira uma pupla:
nomes = 'Maria', 'Helena', 'Luiz'
nomes[1] = "outro"
#para converter lista em tupla:
#nomes = tuple(nomes) ou vise versa list(nomes)

_, _, nome3, *_ = nomes
