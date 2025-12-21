# lista usando dicionario
lista_tarefas = []

#função para cadastrar tarefa
def adicionar_tarefa():
     
     Nome = input('Digite o nome da sua tarefa: ')
     Descricao = input('Descreva sua tarefa: ')
     Status = input('Qual o status da sua tarefa?\n 1. Disponivel\n 2. Fazendo\n 3. Feito\n' )
     tarefa = {'Nome': Nome, 'Descricao': Descricao, 'Status': Status}
     lista_tarefas.append(tarefa)
     print(f'Tarefa {Nome} adicionada com sucesso!')
adicionar_tarefa()

# lembrar de colocar listar todas as terefas, listar por status e listar quantas tarefas foram cadastradas


