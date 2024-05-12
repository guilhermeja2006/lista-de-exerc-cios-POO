from Ingresso import Ingresso
from IngressoVIP import IngressoVIP

vomum: str
VIP: str

comum = Ingresso(5.00)
vip = IngressoVIP(5,4)

print(f"temos dois tipos de ingresso, o comum e o VIP: \n Ingresso comum = {comum.get_valor()} \n Ingresso VIP = {vip.valor_vip()} \n Como voce pode ver a difereça e de: {vip.get_adicional()}")
print("=================================================")
qual = int(input("qual o ingresso que voce deseja: \n 1: Ingresso comum \n 2: Ingresso VIP \n digite 1 ou 2:"))

def ingresso():
  
    if qual == 1:
        return 'comum'
    if qual == 2:
        return 'VIP'
    else:
        print("Ingresso não exitente!!!!")

def ingresso_valor(qual):
    if qual == 1:
        return comum.get_valor()
    if qual == 2:
        return vip.valor_vip()
    
print(f"O ingresso escolhido foi {ingresso()} com o valor de {ingresso_valor(qual)}")
