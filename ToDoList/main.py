import pickle

class ToDoList:
    def __init__(self):
        self.tasks = []

    def list_tasks(self):
        for task in self.tasks:
            print(f"{task['id']}. {task['description']} [{task['status']}]")

    def add_task(self, description):
        if description[0].isupper():
            new_task = {'id': len(self.tasks) + 1, 'description': description, 'status': ' '}
            self.tasks.append(new_task)
            print("Tarefa registrada!!!")
        else:
            print("A descrição da tarefa deve começar com maiúscula.")

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id and task['status'] == ' ':
                task['status'] = 'x'
                self.tasks.remove(task)
                self.tasks.insert(0, task)
                print("Tarefa realizada!!!")
                return
        print("Tarefa não encontrada ou já realizada.")

    def edit_task(self, task_id, new_description):
        for task in self.tasks:
            if task['id'] == task_id:
                task['description'] = new_description
                print("Tarefa editada!!!")
                return
        print("Tarefa não encontrada.")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            print("Arquivo não encontrado. Criando um novo.")

# Função para interação com o usuário
def main():
    todo_list = ToDoList()
    todo_list.load_from_file("todolist.pkl")

    while True:
        print("\n--- ToDoList ---")
        print("1. Listar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Marcar Tarefa como Realizada")
        print("4. Editar Tarefa")
        print("5. Salvar e Sair")

        choice = input("Escolha uma opção (1-5): ")

        if choice == '1':
            todo_list.list_tasks()
        elif choice == '2':
            description = input("Digite a descrição da tarefa: ")
            todo_list.add_task(description)
        elif choice == '3':
            task_id = int(input("Digite o ID da tarefa a ser marcada como realizada: "))
            todo_list.mark_completed(task_id)
        elif choice == '4':
            task_id = int(input("Digite o ID da tarefa a ser editada: "))
            new_description = input("Digite a nova descrição da tarefa: ")
            todo_list.edit_task(task_id, new_description)
        elif choice == '5':
            todo_list.save_to_file("todolist.pkl")
            print("Tarefas salvas. Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
