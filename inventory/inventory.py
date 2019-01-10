# Product Inventory Project for inventory valuation
# sum of inventory values = sum of the cost associated with the products


class Product:
    def __init__(self, id, price, quantity):
        self.id = id
        self.price = price
        self.quantity = quantity


class Inventory:

    def __init__(self, products):  # constructor
        self.products = products

    def inventory_value(self):  # calculation of the inventory value
        total = 0
        for product in self.products:
            total = total + product.quantity * product.price  # inventory value by considering price and quantity
            return total


def outcome():
    product1 = Product('abc123', 500, 2)
    product2 = Product('def456', 100, 1)
    inventory1 = Inventory([product1])
    inventory2 = Inventory([product2])
    print(inventory1.inventory_value() + inventory2.inventory_value())

outcome()

