# LISTA DE TAREFAS
tarefas = []

# Adicionar tarefa
def add_tarefa(tarefa):
    tarefas.append({"tarefa": tarefa, "concluida": False})
    print("Tarefa adicionada: ", tarefa)

# Remover tarefa
def remove_tarefa(tarefa):
    for t in tarefas:
        if t["tarefa"] == tarefa:
            tarefas.remove(t)
            print("Tarefa removida:", tarefa)
            return
    print("Tarefa não encontrada.")

# Concluir tarefa
def concluir_tarefa(tarefa):
    for t in tarefas:
        if t["tarefa"] == tarefa:
            t["concluida"] = True
            print("\n--> Tarefa concluída:", tarefa)
            return
    print("Tarefa não encontrada")

# Exibir tarefas
def list_tarefas():
    if tarefas:
        print("\n--> Lista de tarefas <--")
        for t in tarefas:
            status = "concluída" if t["concluida"] else "pendente"
            print(f"{t['tarefa']} - ({status})")
    else:
        print("\nSem tarefas no momento.")

# Limpar lista
def clear_list():
    tarefas.clear()
    print("Todas as tarefas foram removidas.")

# Selecionar
while True:
    print("\n---> Gerenciador de Tarefas <---")
    print(" 1-Adicionar tarefa")
    print(" 2-Concluir tarefa")
    print(" 3-Remover tarefa")
    print(" 4-Exibir tarefas")
    print(" 5-Limpar lista de tarefas")
    print(" 0-Sair")

    opcao = input("\nDigite a opção desejada ==> ")
    if opcao == "0":
        print("\n...Encerrando o gerenciador de tarefas")
        break

    elif opcao == "1":
        tarefa_nome = input("Digite o nome da tarefa ==> ")
        add_tarefa(tarefa_nome)

    elif opcao == "2":
        tarefa_nome = input("Digite o nome da tarefa que deseja concluir ==> ")
        concluir_tarefa(tarefa_nome)

    elif opcao == "3":
        tarefa_nome = input("Digite o nome da tarefa que gostaria de remover ==> ")
        remove_tarefa(tarefa_nome)

    elif opcao == "4":
        list_tarefas()

    elif opcao == "5":
        clear_list()