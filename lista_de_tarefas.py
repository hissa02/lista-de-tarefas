# lista usando dicionario
lista_tarefas = []

#função para cadastrar tarefa
def adicionar_tarefa():
     Nome = input('Digite o nome da sua tarefa: ')
     Descricao = input('Descreva sua tarefa: ')
     Status = input('Qual o status da sua tarefa?\n 1. Disponivel\n 2. Fazendo\n 3. Feito\n' ) 
     if Status == '1':
        Status = 'Disponivel'
     elif Status == '2':
        Status = 'Fazendo'
     elif Status == '3':
        Status = 'Feito'
     tarefa = {'Nome': Nome, 'Descricao': Descricao, 'Status': Status}
     lista_tarefas.append(tarefa)
     print(f'Tarefa {Nome} adicionada com sucesso!')

#fução para listar tarefas
def listar_tarefas():
     if lista_tarefas:
        print("Lista de tarefas:")
        for tarefa in lista_tarefas:
            print(f"-Nome: {tarefa['Nome']}, Descrição: {tarefa['Descricao']}, Status: {tarefa['Status']}")
     else:
        print("Nenhuma tarefa encontrada.\nAdicione a tarefa primeiro")
      
#função para listar por status
def listar_por_status():
  status = input("Digite o status da tarefa que deseja buscar:\n 1. Disponivel\n 2. Fazendo\n 3. Feito\n ")
  if status == '1':
        status = 'Disponivel'
  elif status == '2':
        status = 'Fazendo'
  elif status == '3':
        status = 'Feito'
  for tarefa in lista_tarefas:
      if tarefa["Status"] == status:
        print("As tarefas presentes nesse status são: ")
        for chave, valor in tarefa.items():
         print(f"{chave}: {valor}")

#função para alterar o status da tarefa
def alterar_status():
  nome = input("Digite nome da tarefa que deseja alterar: ")
  for tarefa in lista_tarefas:
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
def excluir_tarefa():
  nome = input("Digite o nome da tarefa que deseja excluir: ")
  for tarefa in lista_tarefas:
    if tarefa["Nome"] == nome:
      print("Tarefa encontrada:")
      for chave, valor in tarefa.items():
       print(f"{chave}: {valor}")
      lista_tarefas.remove(tarefa)
      print("Tarefa excluída com sucesso.")
      return
  else:
    print('Tarefa não encontrada')

#menu de opções
print("-" * 35)
print('Menu:\n Opção 1: Adicionar Tarefas.\n Opção 2: Listar tarefas.\n Opção 3: Listar tarefas por status.\n Opção 4: Alterar o status da tarefa.\n Opção 5: Excluir tarefa.\n Opção 6: Sair')
print("-" * 35)

while True:
        
  opção = input("Digite a opção desejada: ")
  print()
  
  if opção == '1':
   adicionar_tarefa()

  elif opção == '2':
    listar_tarefas()

  elif opção == '3':
    listar_por_status()

  elif opção == '4':
   alterar_status()
    
  elif opção == '5':
    excluir_tarefa()  
    
  elif opção == '6':
    print("Obrigado por usar o sistema!")
    break
  else:
    print("Opção inválida, por favor, digite um número presente no menu")