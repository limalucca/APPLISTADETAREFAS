tasks = {}

import re

#Validação de data
def validate_date(date_string):
    pattern = r'^\d{2}/\d{2}/\d{4}$'

    if re.match(pattern, date_string):
        return True
    else:
        return False

#Sempre Salvar o arquivo
def save_tasks_to_file():
    with open("tasks.txt", "w") as file:
        for name, description in tasks.items():
            file.write(f"{name}:{description}\n")
    print("Tarefas salvas no arquivo.")

def load_tasks_from_file():
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                name, description = line.strip().split(":")
                tasks[name] = description
        print("Tarefas carregadas no arquivo!")
    except FileNotFoundError:
        print("Arquivo de tarefas não encontrados!")



load_tasks_from_file() #Carrega tarefas do arquivo ao iniciar o APP

#Funções e Menu & Validação de Entrada

def add_task():
    while True:
        name = input("Digite o nome da tarefa: ")
        if not name:
            print("Nome da tarefa não pode estar vazio.")
            continue
        
        if name in tasks:
            print("Essa tarefa já existe.")
            continue
        while True:
            due_date = input("Digite a data de vencimento (dd/mm/aaaa)")

            if not validate_date(due_date):
                print("Formato de data invalido. Use dd/mm/aaaa")
            else:
                break

        description = input("Digite a descrição da tarefa: ")
        tasks[name] = {"due_date":due_date, "description":description}
        print("Tarefa adicionada com sucesso!")
        break

def list_tasks():
    print('Lista de Tarefas:'"\n")
    for name, description in tasks.items():
        print(f"Nome: {name}\nDescrição: {description}\n")
    
def delete_task():
    name = input("Digite o nome da tarefa que deseja excluir: ""\n")
    if name in tasks:
        del tasks[name]
        print('Tarefa excluida com sucesso!')
    else:
        print('Tarefa não encontrada!')

def edit_task():
    name = input("Digite o nome da tarefa que deseja editar: ""\n")
    
    if name in tasks:
        while True:
            new_description = input("Digite a nova descrição da tarefa: ""\n")
            if new_description:
                tasks[name] = new_description
                print("Tarefa editada com sucesso!")
                break
            else:
             print("A descrição não pode estar vazia. Tente novamente.")
    else:
        print("Tarefa não encontrada.")


#Menu de opções.
while True:
    print("Menu:")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Editar Tarefa")
    print("4. Excluir Tarefa")
    print("5. Sair")

    choice = input("Escolha uma opção: ""\n")

    if choice == "1":
        add_task()
        save_tasks_to_file()
        print("\n")
    elif choice == "2":
        list_tasks()
        print("\n")
    elif choice == "3":
        edit_task()
        save_tasks_to_file()
        print("\n")
    elif choice == "4":
        delete_task()
        save_tasks_to_file()
        print("\n")
    elif choice == "5":
        print("Saindo do aplicativo.")
        save_tasks_to_file()
        print("\n")
        break
    else:
        print("Opção inválida. Escolha novamente.")