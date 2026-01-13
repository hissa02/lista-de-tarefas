from classe.tarefa import Tarefa
from classe.fabrica_status import FabricaStatus

class ControladorTarefas:
    # aplicando o padrão singleton
    _instancia = None  # garante uma unica instancia da classe

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.lista_tarefas = []
        return cls._instancia  # Sempre retorna a mesma instância

    # função para cadastrar tarefa
    def adicionar_tarefa(self):
        nome = input('Digite o nome da sua tarefa: ')
        descricao = input('Descreva sua tarefa: ')
        status = input('Qual o status da sua tarefa?\n 1. Disponível\n 2. Fazendo\n 3. Feito\n')
        status = FabricaStatus.criar_status(status)
        tarefa = Tarefa(nome, descricao, status)
        self.lista_tarefas.append(tarefa)
        print(f'Tarefa {nome} adicionada com sucesso!')

    # fução para listar tarefas
    def listar_tarefas(self):
        if self.lista_tarefas:
            print("Lista de tarefas:")
            for tarefa in self.lista_tarefas:
                print(f"Nome: {tarefa.nome}, Descrição: {tarefa.descricao}, Status: {tarefa.status}\n")
        else:
            print("Nenhuma tarefa encontrada.\nAdicione a tarefa primeiro")

    # função para listar por status
    def listar_por_status(self):
        status = input("Digite o status da tarefa que deseja buscar:\n 1. Disponível\n 2. Fazendo\n 3. Feito\n ")
        status_atual = FabricaStatus.criar_status(status)
        print("As tarefas presentes nesse status são: ")
        for tarefa in self.lista_tarefas:
            if tarefa.status == status_atual:
                print(f"Nome: {tarefa.nome}, Descrição: {tarefa.descricao}, Status: {tarefa.status}")
                return
        print(f"\nNenhuma tarefa encontrada com o status '{status_atual}'.")

    # função para alterar o status da tarefa
    def alterar_status(self):
        nome = input("Digite nome da tarefa que deseja alterar o status: ")
        for tarefa in self.lista_tarefas:
            if tarefa.nome == nome:
                print("Tarefa encontrada:")
                print(f" Nome: {tarefa.nome},\n Descrição: {tarefa.descricao}\n Status: {tarefa.status}\n")
                novo_status = input("Digite o novo status da tarefa: \n 1. Disponível\n 2. Fazendo\n 3. Feito\n ")
                novo_status = FabricaStatus.criar_status(novo_status)
                tarefa.mudar_status(novo_status)
                print("Status da tarefa alterado com sucesso.")
                return
        else:
            print("Tarefa não encontrada.")

    # função para excluir tarefa
    def excluir_tarefa(self):
        nome = input("Digite o nome da tarefa que deseja excluir: ")
        for tarefa in self.lista_tarefas:
            if tarefa.nome == nome:
                print("Tarefa encontrada:")
                print(f"Nome: {tarefa.nome}, Descrição: {tarefa.descricao}, Status: {tarefa.status}")
                self.lista_tarefas.remove(tarefa)
                print("Tarefa excluída com sucesso.")
                return
        else:
            print('Tarefa não encontrada')
