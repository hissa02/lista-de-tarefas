# lista usando dicionario
lista_tarefas = []

#função para cadastrar tarefa
def adicionar_tarefa():
     
     Nome = input('Digite o nome da sua tarefa: ')
     Descricao = input('Descreva sua tarefa: ')
     Status = input('Qual o status da sua tarefa?\n 1. Disponivel\n 2. Fazendo\n 3. Feito\n' ) #lembrar de colocar essa parte como se fosse um menu 
     tarefa = {'Nome': Nome, 'Descricao': Descricao, 'Status': Status}
     lista_tarefas.append(tarefa)
     print(f'Tarefa {Nome} adicionada com sucesso!')
adicionar_tarefa()

#fução para listar tarefas
def listar_tarefas():
     if lista_tarefas:
        print("Lista de obras:")
        for tarefa in lista_tarefas:
            print(f"-Nome: {tarefa['Nome']}, Descrição: {tarefa['Descricao']}, Status: {tarefa['Status']}")
     else:
        print("Nenhuma tarefa encontrada.\nAdicione a tarefa primeiro")
      

# lembrar de colocar listar por status e listar quantas tarefas foram cadastradas


