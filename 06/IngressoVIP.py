from Ingresso import Ingresso

class IngressoVIP(Ingresso):
    def __init__(self, valor , adicional) -> None:
        super().__init__(valor)
        self.adicional = adicional

    def get_adicional(self):
        return self.adicional
    
    def set_adicionado(self, adicional):
        self.adicional = adicional

    def valor_vip(self):
        return self.valor +  self.adicional
    
#vip = IngressoVIP(5,4)
#print(vip.valor_vip())