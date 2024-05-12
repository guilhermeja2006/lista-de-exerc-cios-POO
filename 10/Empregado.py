class Empregado:
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getSalario(self):
        return self._salario

    def setSalario(self, salario):
        self._salario = salario

    def toString(self):
        return f'Nome: {self.nome}, Salário: {self._salario}'
