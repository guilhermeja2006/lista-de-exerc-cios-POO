from Gerente import Gerente
from Vendedor import Vendedor

def solicitar_informacoes():
    tipo_empregado = input("Digite o tipo de empregado (gerente/vendedor): ")
    nome = input("Digite o nome: ")
    salario = float(input("Digite o salário: "))

    if tipo_empregado.lower() == 'gerente':
        departamento = input("Digite o departamento: ")
        empregado = Gerente(nome, salario, departamento)
    elif tipo_empregado.lower() == 'vendedor':
        comissao = float(input("Digite a comissão (%): "))
        empregado = Vendedor(nome, salario, comissao)
    
    else:
        print("Tipo de empregado inválido.")
        return

    print(empregado.toString())

if __name__ == "__main__":
    solicitar_informacoes()
