from Funcionario import Funcionario

nome_funci = str(input("Qual o seu nome?"))
salario_funci = float(input("Qual o seu salario?"))
cargo_funci = str(input("qual o seu cargo?"))
desconto_funci = float(input("qual o valor de desconto pro mes alem do IR e INSS?"))
beneficio_funci = float(input("qual o valor de beneficio pro mes?"))

funci = Funcionario(nome= nome_funci,  salario= salario_funci, cargo= cargo_funci, descontos= desconto_funci, beneficios= beneficio_funci)
print("___________DADOS__________")
print(f"nome:{funci.nome}")
print(f"cargo:{funci.cargo}")
print(f"salario broto:{funci.salario}")
print(f"total de IR:{funci.ir()}")
print(f"total de INSS:{funci.inss()}")
print(f"total de descontos:{funci.totalTributos()}")
print(f"beneficios:{funci.beneficios}")
print(f"salario liquido:{funci.salarioLiquido()}")