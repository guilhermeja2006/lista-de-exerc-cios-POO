from Empregado import Empregado

class Vendedor(Empregado):
    def __init__(self, nome, salario, comissao):
        super().__init__(nome, salario)
        self.comissao = comissao

    def getComissao(self):
        return self.comissao

    def setComissao(self, comissao):
        self.comissao = comissao

    def calcularSalario(self):
        return self._salario + (self._salario * self.comissao / 100)

    def toString(self):
        return f'{super().toString()}, Salário com comissão: {self.calcularSalario()}, Comissão: {self.comissao}%'
