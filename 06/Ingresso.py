class Ingresso():
    def __init__(self, valor) -> None:
        self.valor = valor
        
    def get_valor(self):
        return self.valor
    
    def set_valor(self,valor):
        self.valor = valor

ingresso = Ingresso(5.00)

#print(ingresso.get_valor())