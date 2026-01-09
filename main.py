from gerenciar_tarefas import gerenciar_tarefas

# cria uma instância do gerenciador
gerenciador = gerenciar_tarefas()

# menu simples para testar
while True:
    print("\nMenu:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Listar tarefas por status")
    print("4. Alterar status de uma tarefa")
    print("5. Excluir tarefa")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        gerenciador.adicionar_tarefa()
    elif opcao == "2":
        gerenciador.listar_tarefas()
    elif opcao == "3":
        gerenciador.listar_por_status()
    elif opcao == "4":
        gerenciador.alterar_status()
    elif opcao == "5":
        gerenciador.excluir_tarefa()
    elif opcao == "6":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
