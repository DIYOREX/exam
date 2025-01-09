class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def save(self):
      
        print(f"Product saved: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

product = Product("Laptop", 1500, 5)

product.save()
