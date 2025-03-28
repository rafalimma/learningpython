lista_tarefas = []

def adicionar_tarefa():
    tarefa = input("Digite a sua tarefa: ")
    status = "pendente"
    id = len(lista_tarefas) + 1
    nova_tarefa = {"id": id, "descricao": tarefa, "status": status}
    lista_tarefas.append(nova_tarefa)
    print('tarefa adicionada com sucesso!')

def listar_tarefa():
    if len(lista_tarefas) == 0:
        print("LISTA DE TAREFAS VAZIA, ADICIONE UMA TAREFA: ")
        adicionar_tarefa()
    else:
        print("___TAREFAS___")
        for tarefa in lista_tarefas:
            print(f"{tarefa['id']} | {tarefa['descricao']} | {tarefa['status']}")

def remover_tarefa(id_tarefa):
    tarefa = lista_tarefas[id_tarefa - 1]
    lista_tarefas.remove(tarefa)
    print('tarefa removida com sucesso!')

def concluir_tarefa(id_tarefa):
    tarefa = lista_tarefas[id_tarefa - 1]
    tarefa["status"] = "concluída"
    print('tarefa concluída!')

while True:
    print()
    print('Gerenciador de tarefas')
    print("Adicionar tarefa 1 \n Remover tarefa 2 \n Listar tarefas 3 \n Marcar como conluída 4 \n Sair 5")
    opc = input("escolha uma opção: ")
    if opc == "1":
        adicionar_tarefa()
    elif opc == "2":
        id_tarefa = input("Digite o id da tarefa que deseja remover: ")
        int_tarefa = int(id_tarefa)
        remover_tarefa(int_tarefa)
    elif opc == "3":
        listar_tarefa()
    elif opc == "4":
        id_tarefa = input("Digite o id da tarefa que deseja concluir: ")
        int(id_tarefa)
        int_tarefa = int(id_tarefa)
        concluir_tarefa(int_tarefa)
    elif opc == "5":
        exit()
