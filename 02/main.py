from Retangulo import Retangulo


largura_ret = float(input("Digite a largura do retângulo: "))
altura_ret = float(input("Digite a altura do retângulo: "))

ret = Retangulo(largura=largura_ret, altura=altura_ret)
print(f"Área do retângulo: {ret.area()}")
print(f"Perímetro do retângulo: {ret.perimetro()}")
