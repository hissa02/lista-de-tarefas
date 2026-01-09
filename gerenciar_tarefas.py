from tarefa import Tarefa

class gerenciar_tarefas:
    def __init__(self):
        self.lista_tarefas = []       

    #função para cadastrar tarefa
    def adicionar_tarefa(self):
        nome = input('Digite o nome da sua tarefa: ')
        descricao = input('Descreva sua tarefa: ')
        status = input('Qual o status da sua tarefa?\n 1. Disponivel\n 2. Fazendo\n 3. Feito\n' ) 
        if status == '1':
            status = 'Disponivel'
        elif status == '2':
            status = 'Fazendo'
        elif status == '3':
            status = 'Feito'
        tarefa = {'Nome': nome, 'Descricao': descricao, 'Status': status}
        self.lista_tarefas.append(tarefa)
        print(f'Tarefa {nome} adicionada com sucesso!')

    #fução para listar tarefas
    def listar_tarefas(self):
        if self.lista_tarefas:
            print("Lista de tarefas:")
            for tarefa in self.lista_tarefas:
                print(f"-Nome: {tarefa['Nome']}, Descrição: {tarefa['Descricao']}, Status: {tarefa['Status']}")
        else:
            print("Nenhuma tarefa encontrada.\nAdicione a tarefa primeiro")
      
#função para listar por status
    def listar_por_status(self):
        status = input("Digite o status da tarefa que deseja buscar:\n 1. Disponivel\n 2. Fazendo\n 3. Feito\n ")
        if status == '1':
            status = 'Disponivel'
        elif status == '2':
            status = 'Fazendo'
        elif status == '3':
            status = 'Feito'
        for tarefa in self.lista_tarefas:
            if tarefa["Status"] == status:
                print("As tarefas presentes nesse status são: ")
                for chave, valor in tarefa.items():
                    print(f"{chave}: {valor}")
                break  
        else:
            print(f"Nenhuma tarefa encontrada com o status '{status}'.")

    #função para alterar o status da tarefa
    def alterar_status(self):
        nome = input("Digite nome da tarefa que deseja alterar: ")
        for tarefa in self.lista_tarefas:
            if tarefa["Nome"] == nome: 
                print("Tarefa encontrada:")
                print(f"Nome: {tarefa['Nome']},\n Descrição: {tarefa['Descricao']},\n Status: {tarefa['Status']}")
                novo_status = input("Digite o novo status da tarefa: \n 1. Disponivel\n 2. Fazendo\n 3. Feito\n ")
                if novo_status == '1':
                    novo_status = 'Disponivel'
                elif novo_status == '2':
                    novo_status = 'Fazendo'
                elif novo_status == '3':
                    novo_status = 'Feito'
                tarefa["Status"] = novo_status
                print("Tarefa alterada com sucesso.")
                return
        else:
            print("Tarefa não encontrada.")

    #função para excluir tarefa
    def excluir_tarefa(self):
        nome = input("Digite o nome da tarefa que deseja excluir: ")
        for tarefa in self.lista_tarefas:
            if tarefa["Nome"] == nome:
                print("Tarefa encontrada:")
                for chave, valor in tarefa.items():
                    print(f"{chave}: {valor}")
                self.lista_tarefas.remove(tarefa)
                print("Tarefa excluída com sucesso.")
                return
        else:
            print('Tarefa não encontrada')
