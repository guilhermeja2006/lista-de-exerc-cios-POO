from Bomba_combustivel import Bomba_combustivel

def solicitar_informacoes():
    tipo_combustivel = input("Digite o tipo de combustível: ")
    valor_litro = float(input("Digite o valor do litro: "))
    bomba = Bomba_combustivel(tipo_combustivel, valor_litro)

    while True:
        print("\n1. Abastecer por valor")
        print("2. Abastecer por litro")
        print("3. Alterar valor do litro")
        print("4. Alterar quantidade de combustível")
        print("5. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            valor = float(input("Digite o valor a ser abastecido: "))
            print(f'Litros colocados no veículo: {bomba.abastecer_por_valor(valor)}')
        elif opcao == 2:
            litros = float(input("Digite a quantidade em litros de combustível: "))
            print(f'Valor a ser pago pelo cliente: {bomba.abastecer_por_litro(litros)}')
        elif opcao == 3:
            valor = float(input("Digite o novo valor do litro: "))
            bomba.alterar_valor_litro(valor)
        elif opcao == 4:
            quantidade = float(input("Digite a nova quantidade de combustível: "))
            bomba.alterar_quantidade_combustivel(quantidade)
        elif opcao == 5:
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    solicitar_informacoes()
