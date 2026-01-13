# Classe que aplica o padrão Factory para criar o status da tarefa
class FabricaStatus:
    @staticmethod
    def criar_status(numero):
        if numero == '1':
            return "Disponível"
        elif numero == '2':
            return "Fazendo"
        elif numero == '3':
            return "Feito"
        else:
            return "Status Inválido"
