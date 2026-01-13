from controlador.controlar_tarefas import ControladorTarefas

# cria uma instância do controlador
controlador = ControladorTarefas()

# menu simples para testar
while True:
    print("\nMENU\n1.Adicionar\n2.Listar\n3.Listar por status\n4.Alterar\n5.Excluir\n6.Sair")
    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        controlador.adicionar_tarefa()
    elif opcao == "2":
        controlador.listar_tarefas()
    elif opcao == "3":
        controlador.listar_por_status()
    elif opcao == "4":
        controlador.alterar_status()
    elif opcao == "5":
        controlador.excluir_tarefa()
    elif opcao == "6":
        print("Obrigado por usar o sistema!")
        break
    else:
        print("Opção inválida, escolha um numero entre 1 e 6.")
