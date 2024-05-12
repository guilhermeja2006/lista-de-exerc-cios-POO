class Empregado:
    def __init__(self, primeiro_nome, sobrenome, salario_mensal):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.salario_mensal = max(0, salario_mensal)

    def getPrimeiroNome(self):
        return self.primeiro_nome

    def setPrimeiroNome(self, primeiro_nome):
        self.primeiro_nome = primeiro_nome

    def getSobrenome(self):
        return self.sobrenome

    def setSobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def getSalarioMensal(self):
        return self.salario_mensal

    def setSalarioMensal(self, salario_mensal):
        self.salario_mensal = max(0, salario_mensal)

    def salarioAnual(self):
        return self.salario_mensal * 12

    def aumentarSalario(self, percentual):
        self.salario_mensal *= (1 + percentual / 100)
