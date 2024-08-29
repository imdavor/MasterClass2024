# 177. Inheritance
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_data(self):
        self.name = input('Enter product name: ')
        self.price = input('Enter product price: ')

    def put_data(self):
        print(f'Product name: {self.name}\nProduct price: {self.price}')


class DigitalProduct(Product):  # inherit from Product class
    def __init__(self, link):
        self.link = link

    def get_link(self):
        self.link = input('Enter product link: ')

    def put_link(self):
        print(f'Product link: {self.link}')


ebook = DigitalProduct("")
ebook.get_data()
ebook.get_link()
ebook.put_data()
ebook.put_link()

# 176. Functional & OOP Based Way Of Writing Code


# def product_data():
#     product_name = input('Enter product name: ')
#     product_price = input('Enter product price: ')
#     print(product_name, product_price)
#
#

# product_data()

# ovako to izgleda u OOPu

"""class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_data(self):
        self.name = input('Enter product name: ')
        self.price = input('Enter product price: ')

    def put_data(self):
        print(f'Product name: {self.name}, Product price: {self.price}')


p1 = Product("", "")
p1.get_data()
p1.put_data()"""

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
