"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

lista_a = ['Luiz', 'Maria']
lista_b = lista_a
#pode copiar a lista a na lista b usando .copy:
lista_b = lista_a.copy()
# está fazendo as duas variáveis apontarem para um mesmo valor na memória

lista_a[0] = 'qualquer coisa' #isso acaba alterando a lista b
print(lista_a)
print(lista_b)
