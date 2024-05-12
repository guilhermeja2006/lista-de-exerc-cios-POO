class Data():
    def __init__(self,dia: int, mes: int, ano: int) -> None:
        self.dia = dia
        self.mes = mes
        self.set_ano(ano)

    def get_dia(self):
        return self.dia
    
    def set_dia(self, dia):
        self.dia = dia

    def get_mes(self):
        return self.mes
    
    def set_mes(self,mes):
        self.mes = mes

    def get_ano(self):
        return self.ano
    
    def set_ano(self, ano):
        if len(str(ano)) == 4:
            self.ano = ano
        else:
            print("O ano deve ter 4 dígitos.")

    def displayData(self):
        return f"{self.dia}/{self.mes}/{self.ano}"

#d = Data(1,9,2006)

#print(f"{d.displayData()}")