# class product
# data: name & price
# functionality: show information for this product

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_product(self):
        print(f'{self.name} {self.price:.2f}')
