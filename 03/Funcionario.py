class Funcionario():
    def __init__(self, nome, salario, cargo, descontos, beneficios) -> None:
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
        self.descontos = descontos
        self.beneficios = beneficios

    def inss(self):
        if self.salario<1300:
            return self.salario / 100 * 7.5
        if self.salario > 1300 and self.salario < 2570:
            return self.salario / 100 * 9
        if self.salario > 2570 and self.salario < 3800:
            return self.salario / 100 * 12
        if self.salario > 3800 and self.salario < 7500:
            return self.salario / 100 * 14
        if self.salario > 7500 and self.salario < 12800:
            return self.salario / 100 * 14.5
        if self.salario > 12800 and self.salario < 25700:
            return self.salario / 100 * 16.5
        if self.salario > 25700 and self.salario < 50140:
            return self.salario / 100 * 19
        if self.salario > 50140:
            return self.salario / 100 * 22     
    
    def ir(self):
        if self.salario < 2100:
            return 0
        if self.salario > 2100 and self.salario < 2830:
            return self.salario / 100 * 7.5
        if self.salario > 2830 and self.salario < 3750:
            return self.salario / 100 * 15
        if self.salario > 3750 and self.salario < 4665:
            return self.salario / 100 * 22.5
        if self.salario > 4665:
            return self.salario / 100 * 27.5
        
    def totalTributos(self):
        return self.descontos + self.inss() + self.ir()

    def salarioLiquido(self):
        return self.salario - self.totalTributos()  + self.beneficios
        
