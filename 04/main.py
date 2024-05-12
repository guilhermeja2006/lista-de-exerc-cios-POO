from Empregado import Empregado



e1 = Empregado("","",0.0)
e2 = Empregado("","",0.0)

print("Empregado 01:")

nom = str(input("Digite seu nome:"))
e1.set_nome(nom)

sobrNome = str(input("Digite o seu sobre nome:"))
e1.set_sebrenome(sobrNome)

sal = float(input("Digite o seu salario:"))
e1.set_selario(sal)

print("-------------------------")

print("Empregado 02:")

nom = str(input("Digite seu nome:"))
e2.set_nome(nom)

sobrNome = str(input("Digite o seu sobre nome:"))
e2.set_sebrenome(sobrNome)

sal = float(input("Digite o seu salario:"))
e2.set_selario(sal)

print("*************************")
print("ATUALIZAÇÃO DE DAOS:")
print(f"Nome: {e1.get_nome()}")
print(f"Sobrenome: {e1.get_sobrenome()}")
print(f"Salario antigo: {e1.get_selario()}")
print(f"Salário com almento: {e1.almento()}")
print("-------------------------")
print(f"Nome: {e2.get_nome()}")
print(f"Sobrenome: {e2.get_sobrenome()}")
print(f"Salario antigo: {e2.get_selario()}")
print(f"Salário com almento: {e2.almento()}")
print("-------------------------")