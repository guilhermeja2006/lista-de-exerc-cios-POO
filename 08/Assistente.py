from Funcionario import Funcionario

class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula

    def setMatricula(self, matricula):
        self.matricula = matricula

    def exibeDados(self):
        return f'{super().exibeDados()}, Matrícula: {self.matricula}'

