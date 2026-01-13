class Tarefa:
    def __init__(self, nome, descricao, status):
        self.nome = nome
        self.descricao = descricao
        self.status = status

    def mudar_status(self, novo_status):
        self.status = novo_status
