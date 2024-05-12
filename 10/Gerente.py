from Empregado import Empregado

class Gerente(Empregado):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def toString(self):
        return f'{super().toString()}, Departamento: {self.departamento}'
