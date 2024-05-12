class Empregado(): 
    def __init__(self, nomeEmpregado, sobrenomeEmpregado, salarioEmpregado) -> None:
        self.nomeEmpregado =  nomeEmpregado
        self.sobrenomeEmpregado = sobrenomeEmpregado
        self.salarioEmpregado = salarioEmpregado

    def get_nome(self):
        return self.nomeEmpregado
    
    def set_nome(self, nome):
        self.nomeEmpregado = nome

    def get_sobrenome(self):
        return self.sobrenomeEmpregado
    
    def set_sebrenome(self, sobrenome):
        self.sobrenomeEmpregado = sobrenome

    def get_selario(self):
        return self.salarioEmpregado
    
    def set_selario(self, salario):
        self.salarioEmpregado = salario

    def almento(self):
        return self.salarioEmpregado / 100 *10 + self.salarioEmpregado

