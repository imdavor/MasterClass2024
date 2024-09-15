# 191. Entire OOP Example Part 2
class Vehicle:
    # 3. create a constructor
    # creating class atribute
    class_atribute = "This is class attribute."

    def __init__(self, name, color):  # parametri koje koristimo kada dole kreiramo objekt klase
        # self.name = "a"
        # self.color = "b"
        # ako dodamo name i color onda instance varijable izgledaju ovak da ih možemo pass dalje
        self.name = name
        self.color = color

    # kada kreramo metodu u klasi moramo korstiti @dekorator
    @classmethod
    def class_method(cls):
        print('This is class method.')
        print(f'I can access class atribute: {cls.class_atribute}')

    # 4. ovako kreiramo "Instance Method"
    def display_info(self):
        print(f'Vehicle: {self.name}, Color: {self.color}')

        # kada kreiramo static metodu u klasi isto koristimo @dekorator

    @staticmethod
    def static_method():
        print('Im a static method and CANT access anything.')


# 5. Inheritance klasa
class Car(Vehicle):
    # override klasu iz super klase u sub klasi
    def __init__(self, name, color, fuel):
        # ako zelimo override konstruktora, name i color iz super klase
        super().__init__(name, color)
        self.fuel = fuel

    # override metodu iz super klase u sub klasi
    def display_info(self):
        print(f'{self.name}, {self.color}, {self.fuel}')


# 2. kreiramo objekt klase
vehicle = Vehicle("Bmw", "Red")
# a ovo je preko Instance Metode
vehicle.display_info()

# kreiramo objekt 'car' iz 'Car' klase
# nakon overridea klase moramo dodati i fuel
car = Car("C4", "blue", "benzin")
car.display_info()
# access class atribute
print(Vehicle.class_atribute)

# access class method
Vehicle.class_method()
Vehicle.static_method()

# 190. Entire OOP Example Part 1

# 1. create a class
"""class Vehicle:
    # 3. create a constructor
    def __init__(self, name, color):  # parametri koje koristimo kada dole kreiramo objekt klase
        # self.name = "a"
        # self.color = "b"
        # ako dodamo name i color onda instance varijable izgledaju ovak da ih možemo pass dalje
        self.name = name
        self.color = color

    # 4. ovako kreiramo "Instance Method"
    def display_info(self):
        print(f'Vehicle: {self.name}, Color: {self.color}')


# 5. Inheritance klasa
class Car(Vehicle):
    pass


# 2. kreiramo objekt klase
vehicle = Vehicle("Bmw", "Red")
# ovo je print direkt iz klase
print(f'Vehicle: {vehicle.name}, Color: {vehicle.color}')
# a ovo je preko Instance Metode
vehicle.display_info()

# kreiramo objekt 'car' iz 'Car' klase
car = Car("C4", "blue")
car.display_info()"""
