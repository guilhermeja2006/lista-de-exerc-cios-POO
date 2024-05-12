class Invoice:
    def __init__(self, item_number, item_description, item_quantity, item_price):
        self.item_number = item_number
        self.item_description = item_description
        self.item_quantity = item_quantity
        self.item_price = item_price

    def getItemNumber(self):
        return self.item_number

    def getItemDescription(self):
        return self.item_description

    def getItemQuantity(self):
        return self.item_quantity

    def getItemPrice(self):
        return self.item_price

    def toString(self):
        return f'Número do item: {self.item_number}, Descrição: {self.item_description}, Quantidade: {self.item_quantity}, Preço unitário: {self.item_price}'
