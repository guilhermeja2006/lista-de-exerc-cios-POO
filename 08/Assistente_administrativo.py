from Assistente import Assistente

class Assistente_administrativo(Assistente):
    def __init__(self, nome, salario, matricula, turno, adicional_noturno):
        super().__init__(nome, salario, matricula)
        self.turno = turno
        self.adicional_noturno = adicional_noturno

    def ganhoAnual(self):
        if self.turno == 'noite':
            return super().ganhoAnual() + self.adicional_noturno
        else:
            return super().ganhoAnual()
