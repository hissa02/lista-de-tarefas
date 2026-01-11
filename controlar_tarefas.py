from tarefa import Tarefa, Disponivel, Fazendo, Feito

class ControladorTarefas:
#aplicando o padrão singleton
    _instancia = None # garente uma unica instrancia da classe

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.lista_tarefas = []
        return cls._instancia  # Sempre retorna a mesma instância
    
#função para cadastrar tarefa
    def adicionar_tarefa(self):
        nome = input('Digite o nome da sua tarefa: ')
        descricao = input('Descreva sua tarefa: ')
        status = input('Qual o status da sua tarefa?\n 1. Disponivel\n 2. Fazendo\n 3. Feito\n' ) 
        if status == '1':
            estrategia = Disponivel()
        elif status == '2':
            estrategia = Fazendo()
        elif status == '3':
            estrategia = Feito()
        tarefa = Tarefa(nome, descricao, estrategia) 
        self.lista_tarefas.append(tarefa)
        print(f'Tarefa {nome} adicionada com sucesso!')

#fução para listar tarefas
    def listar_tarefas(self):
        if self.lista_tarefas:
            print("Lista de tarefas:")
            for tarefa in self.lista_tarefas:
                print(f"Nome: {tarefa.nome}, Descrição: {tarefa.descricao}, Status: {tarefa.status}\n")
        else:
            print("Nenhuma tarefa encontrada.\nAdicione a tarefa primeiro")
      
#função para listar por status
    def listar_por_status(self):
        status = input("Digite o status da tarefa que deseja buscar:\n 1. Disponivel\n 2. Fazendo\n 3. Feito\n ")
        if status == '1':
            status = Disponivel()
        elif status == '2':
            status = Fazendo()
        elif status == '3':
            status = Feito()
        status_atual = status.definir_status()
        print("As tarefas presentes nesse status são: ")
        for tarefa in self.lista_tarefas:
            if tarefa.status == status_atual:
                print(f"Nome: {tarefa.nome}, Descrição: {tarefa.descricao}, Status: {tarefa.status}")
                return
        print(f"\nNenhuma tarefa encontrada com o status '{status_atual}'.")

#função para alterar o status da tarefa
    def alterar_status(self):
        nome = input("Digite nome da tarefa que deseja alterar o status: ")
        for tarefa in self.lista_tarefas:
            if tarefa.nome == nome: 
                print("Tarefa encontrada:")
                print(f" Nome: {tarefa.nome},\n Descrição: {tarefa.descricao}\n Status: {tarefa.status}\n")
                novo_status = input("Digite o novo status da tarefa: \n 1. Disponivel\n 2. Fazendo\n 3. Feito\n ")
                if novo_status == '1':
                    novo_status = Disponivel()
                elif novo_status == '2':
                    novo_status = Fazendo()
                elif novo_status == '3':
                    novo_status = Feito()
                # aqui convertemos o objeto de status para texto antes de salvar
                tarefa.mudar_status(novo_status.definir_status())   
                print("Status da tarefa alterado com sucesso.")
                return
        else:
            print("Tarefa não encontrada.")

#função para excluir tarefa
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