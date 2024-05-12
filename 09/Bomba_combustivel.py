class Bomba_combustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel=100):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros = valor / self.valor_litro
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            return litros
        else:
            return "Combustível insuficiente na bomba."

    def abastecer_por_litro(self, litros):
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            return litros * self.valor_litro
        else:
            return "Combustível insuficiente na bomba."

    def alterar_valor_litro(self, valor):
        self.valor_litro = valor

    def alterar_quantidade_combustivel(self, quantidade):
        self.quantidade_combustivel = quantidade
