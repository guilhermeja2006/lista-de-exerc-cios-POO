from Invoice import Invoice

def solicitar_informacoes():
    item_number = input("Digite o número do item: ")
    item_description = input("Digite a descrição do item: ")
    item_quantity = int(input("Digite a quantidade comprada do item: "))
    item_price = float(input("Digite o preço unitário do item: "))

    invoice = Invoice(item_number, item_description, item_quantity, item_price)

    print(invoice.toString())

if __name__ == "__main__":
    solicitar_informacoes()
