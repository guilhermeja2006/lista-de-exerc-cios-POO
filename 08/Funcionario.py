class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def addAumento(self, valor):
        self.salario += valor

    def ganhoAnual(self):
        return self.salario * 12

    def exibeDados(self):
        return f'Nome: {self.nome}, Salário: {self.salario}'
