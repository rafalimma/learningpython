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
import json

def adiciona(tarefa, lista):
    lista.append(tarefa)
    return lista

def desfazer(lista):
    lista.pop()
    return lista

def mostrar(tarefas):
    n = 1
    print()
    print('TAREFAS: ')
    for i in tarefas:
        print(f'task {n}: {i}')
        n += 1

def ler(tarefas, caminho_arq):
    dados = []
    try:
        with open(caminho_arq, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except: FileNotFoundError
    print('Arquivo inexistente')
    salvar(tarefas, caminho_arq)
    return dados

def salvar(tarefas, caminho_arq):
    dados = tarefas
    with open(caminho_arq, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
    return dados

CAMINHO_ARQ = 'aula124-exercicio.json'
tarefas = ler([], CAMINHO_ARQ)

print("Comandos: listar, desfazer, refazer, add")


while True:
    comando = input('Digite um comando: ')
    comandos_disponiveis = ['listar', 'desfazer', 'refazer', 'add']
    if comando not in comandos_disponiveis:
        print("Digite apenas comandos disponíveis")
    if comando == 'add':
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
            last = tarefas[-1]
            desfazer(tarefas)
            mostrar(tarefas)
    if comando == 'refazer':
        tarefas.append(last)
        mostrar(tarefas)

    salvar(tarefas, CAMINHO_ARQ)



    


