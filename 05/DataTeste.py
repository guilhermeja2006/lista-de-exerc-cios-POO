from  Data import Data

d = Data(0,0,1000)

dia = int(input("digite o dia:"))
dia = d.set_dia(dia)

mes = int(input("digiteo mes:"))
mes = d.set_mes(mes)

ano = int(input("digite o ano:"))
ano = d.set_ano(ano)

print(f"data igual a :{d.displayData()}")