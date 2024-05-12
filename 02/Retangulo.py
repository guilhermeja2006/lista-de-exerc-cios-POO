class Retangulo():
    def __init__(self,altura, largura)->None:
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.largura * self.altura
       

    def perimetro(self):
        return 2 * (self.largura + self.altura)

#retangulo = Retangulo(altura=5, largura=10)

   
   
