# 189. Using Super to use Parents in Child
# zove def __init__ iz Parent u Child tako da ga Child ne overwrite-a

class Parent:
    def __init__(self):
        self.parent_balance = 50000

    def diplay_balance(self):
        print(f'Parent balance is: {self.parent_balance}')


#

class Child(Parent):
    def __init__(self):
        super().__init__()  # ovo je __init__ iz Parent klase
        self.child_balance = 32000

    def diplay_balance(self):
        print(f'Childs balance is: {self.child_balance} and parents balance is: {self.parent_balance}')
        print(f'Sum balance is: {self.child_balance + self.parent_balance}')


mikie = Child()

mikie.diplay_balance()

# 188. Overriding Superclass Constructor
"""class Parent:
    def __init__(self):
        self.balance = 50000

    def diplay_balance(self):
        print(f'Parent balance is: {self.balance}')


class Child(Parent):
    def __init__(self):
        self.balance = 32000

    def diplay_balance(self):
        print(f'Childs balance is: {self.balance}')


mikie = Child()
joei = Parent()
mikie.diplay_balance()
joei.diplay_balance()
"""
# 187. Constructor Inheritance
"""class Parent:
    def __init__(self):
        self.balance = 50000

    def diplay_balance(self):
        print(f'Parent balance is: {self.balance}')


class Child(Parent):
    pass  # nasljedjuje konstruktor "def __init__" od Parent klase


mikie = Child()
mikie.diplay_balance()
"""
