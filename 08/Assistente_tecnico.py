from Assistente import Assistente

class Assistente_tecnico(Assistente):
    def __init__(self, nome, salario, matricula, bonus):
        super().__init__(nome, salario, matricula)
        self.bonus = bonus

    def ganhoAnual(self):
        return super().ganhoAnual() + self.bonus
