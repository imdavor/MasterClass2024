# 186. Nesting Class Example
class Zoo:
    def __init__(self):  # inicijaliziram Zoo klasu sa praznom listom
        self.animals = []

    # na kraju kreiramo metodu koja ce dodati animal tj koja ce biti veza izmedju klase Animal u listu gore animals
    def add_animal(self, name, species):
        # prvo moramo kreirati animal objekt sa dole klasom Animal
        animal = self.Animal(name, species)
        # sada kada je kreirana animal dodamo je u listu
        self.animals.append(animal)

    class Animal:
        def __init__(self, name, species):
            self.name = name
            self.species = species

        def display_info(self):
            print(f'Animal: {self.name}, Species: {self.species}')


# kada smo definirali klase:
# 1. kreiramo Zoo
my_zoo = Zoo()
# 2. kreiramo i dodamo animal u list
my_zoo.add_animal("Lion", "Cat")
my_zoo.add_animal("Eagle", "Bird")
my_zoo.add_animal("Snake", "Reptile")

# 3. ispis
for animal in my_zoo.animals:
    animal.display_info()
# 185. Nested Classes
"""class Car:
    def __init__(self, brand):
        self.brand = brand
        self.steering_object = self.Steering()  # prvo kreiramo obj of inner class

    @staticmethod  # static methods aren’t bound to an object. In other words, static methods cannot access and
    # modify an object state.
    def drive():
        print('Drive')

    class Steering:
        @staticmethod
        def rotate():
            print('Rotate')


car = Car('Toyota')
car.drive()
# my way
turn = Car.Steering()
turn.rotate()
# tuts way
steer = car.steering_object
steer.rotate()
"""
