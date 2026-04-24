# operação ternária
# Em vez de escrever um bloco inteiro de if, você coloca o resultado desejado primeiro.
nota = 7
status = "Aprovado" if nota >= 7 else "reprovado"

# List Comprehenshion

# O que é: Uma forma de criar uma nova lista baseada em outra lista (ou iterável) de forma muito rápida.

# exemplo lista de leiloeiros
leiloes = ['casa curitiba', 'apartamento cascavel', 'terreno Piraquara', "casa no batel", 'casa Cabral', 'apt Curitiba']

selecionados = []
for l in leiloes:
    if l.startswith('casa'):
            selecionados.append(l)

print(selecionados)
# com List Comprehenshion
selecionadosc = [l for l in leiloes if l.startswith('casa')]
# primeiro o que eu quero no append, depois o for e depois a condição
print(selecionadosc)