from Empregado import Empregado

def solicitar_informacoes():
    primeiro_nome = input("Digite o primeiro nome: ")
    sobrenome = input("Digite o sobrenome: ")
    salario_mensal = float(input("Digite o salário mensal: "))

    empregado = Empregado(primeiro_nome, sobrenome, salario_mensal)

    print(f'Salário anual de {empregado.getPrimeiroNome()} {empregado.getSobrenome()}: {empregado.salarioAnual()}')

    empregado.aumentarSalario(10)

    print(f'Salário anual de {empregado.getPrimeiroNome()} {empregado.getSobrenome()} após aumento de 10%: {empregado.salarioAnual()}')

if __name__ == "__main__":
    solicitar_informacoes()
