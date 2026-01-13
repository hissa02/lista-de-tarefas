from abc import ABC, abstractmethod # para o padrão strategy
#classes de status implementando o padrão strategy
class StrategyStatus(ABC):
    @abstractmethod
    def definir_status(self):
        pass

class Disponivel(StrategyStatus):
    def definir_status(self):
        return "Disponível"

class Fazendo(StrategyStatus):
    def definir_status(self):
        return "Fazendo"

class Feito(StrategyStatus):
    def definir_status(self):
        return "Feito"
    
#classe tarefa
class Tarefa:
    def __init__(self, nome, descricao, strategy_status_definir_status):
        self.nome = nome
        self.descricao = descricao
        self.status = strategy_status_definir_status.definir_status()

    def mudar_status(self, novo_status):
        self.status = novo_status