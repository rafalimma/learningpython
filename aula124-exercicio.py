# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def adiciona(tarefa, lista):
    lista.append(tarefa)
    item = lista.pop()
    lista.append(item)
    return lista

def desfazer(lista):
    lista.pop()
    return lista

def mostrar(tarefas):
    n = 1
    print('TAREFAS: ')
    for i in tarefas:
        print(f'task {n}: {i}')
        n += 1


print("Comandos: listar, desfazer, refazer, adicionar")
tarefas = []
while True:
    comando = input('Digite um comando: ')
    comandos_disponiveis = ['listar', 'desfazer', 'refazer', 'adicionar']
    if comando not in comandos_disponiveis:
        print("Digite apenas comandos disponíveis")
    if comando == 'adicionar':
        tarefa = ''
        while True:
            tarefa = input('Digite uma TAREFA: ')
            if tarefa == 'ok':
                break
            adiciona(tarefa, tarefas)
    if comando == 'listar':
        if len(tarefas) == 0:
            print('Nada para listar.')
        else:
            mostrar(tarefas)
    if comando == 'desfazer':
        if len(tarefas) == 0:
            print('Nada para listar.')
        else:
            desfazer(tarefas)
            mostrar(tarefas)
    if comando == 'desfazer':
        ...
    


