# 176. Functional & OOP Based Way Of Writing Code

# 175. Methods In Object Oriented Programming
"""class Product:
    quantity = 400

    def __init__(self, name,
                 price):
        self.name = name
        self.price = price

    # kreiranje metode za izracun popusta
    # mora imati mnogucnost pristupa konstruktoru
    def summer_discount(self, discount):
        self.price = self.price - self.price * discount / 100

    # summer_discount mora/moze se pozvati samo na objektu


p1 = Product("T-Shirt", 10)
p2 = Product("Phone", 400)
print(f'Product: {p1.name}, Price: ${p1.price}')
print(f'Product: {p2.name}, Price: ${p2.price}')
p1.summer_discount(10)
p2.summer_discount(10)
print(f'Product: {p1.name}, Price "5%discount": ${p1.price}')
print(f'Product: {p2.name}, Price "5%discount": ${p2.price}')""
"""
# 174. Instance Attributes
""""
class Product:
    quantity = 100

    # kreiranje konstruktora
    # metoda; inicijalizacija objekta; "__"< ne smijes zvati; referenca na objekt itself(
    # Product); name, price> instace atributi
    def __init__(self, name,
                 price):
        self.name = name
        self.price = price


p1 = Product("phone", 300)
p2 = Product("laptop", 800)
print(p1.name, p1.price)
print(p2.name, p2.price)"""

# 173. Creating Class & Objects
"""class Product:
    quantity = 100


p1 = Product()
P2 = Product()
print(p1.quantity)
print(p2.quantity)
"""
