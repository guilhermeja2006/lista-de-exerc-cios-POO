from Assistente_tecnico import Assistente_tecnico
from Assistente_administrativo import Assistente_administrativo

def solicitar_informacoes():
    nome = input("Digite o nome: ")
    salario = float(input("Digite o salário: "))
    matricula = input("Digite a matrícula: ")
    tipo = input("Digite o tipo de assistente (tecnico/administrativo): ")

    if tipo.lower() == 'tecnico':
        bonus = float(input("Digite o bônus salarial: "))
        assistente = Assistente_tecnico(nome, salario, matricula, bonus)
    elif tipo.lower() == 'administrativo':
        turno = input("Digite o turno (dia/noite): ")
        adicional_noturno = 0
        if turno.lower() == 'noite':
            adicional_noturno = float(input("Digite o adicional noturno: "))
        assistente = Assistente_administrativo(nome, salario, matricula, turno, adicional_noturno)
    else:
        print("Tipo de assistente inválido.")
        return
    
    print("====================================")
    print(assistente.exibeDados())
    print(f'Ganho anual: {assistente.ganhoAnual()}')

if __name__ == "__main__":
    solicitar_informacoes()
