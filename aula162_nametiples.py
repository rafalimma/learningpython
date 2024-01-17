# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# from collections import namedtuple

from collections import namedtuple

Carta = namedtuple('Carta', ['valor', 'naipe'],
                   defaults=['Valor','Naipe']
                   )
espadas = Carta('A', '♠️')

print(espadas._asdict)
# print(espadas)
# print(espadas.naipe)
# print(espadas.valor)
print(espadas._field_defaults)
for valor in espadas:
    print(valor)
