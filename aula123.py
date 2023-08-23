# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = [] # dentro da função é criado o parametro
    lista.append(nome)
    return lista
# não usar parametros mutáveis em parametros da função
# (padrão)

lista1 = []
cliente1 = adiciona_clientes('rafa')
adiciona_clientes('joana', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('helena')
adiciona_clientes('marta', cliente2)
print(cliente2)
