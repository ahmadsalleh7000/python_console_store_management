class Product:
    def __init__(self, name, price, quantity,id=None):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price} ({self.quantity} available)"
