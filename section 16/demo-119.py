# razmak


"""# Coding Challenge 4
# Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:
# BMI = (weight in Kg)/(Height in Meters)^2.
# Make sure to use a function which accepts the height and weight values and returns the BMI value.
def bmi_calculator(new_weight, new_height):
    bmi = new_weight / new_height ** 2
    return bmi


weight = float(input('Enter weight: '))
height = float(input('Enter height: '))
print(f'Your BMI is {bmi_calculator(weight, height)}')
"""
"""### Solution
def calculate_BMI(new_weight, new_height):
    new_bmi = new_weight / (pow(new_he+ight, 2))
    return new_bmi


weight = float(input('Enter weight in Kgs'))
height = float(input('Enter height in meters'))
bmi = calculate_BMI(weight, height)
print(bmi)
"""
"""# Decorating Functions Returning Values
def summer_total_discount(func):
    def wrapper(price):
        func(price)
        return func(price / 2)

    return wrapper


@summer_total_discount
def total(price):
    return price

print(total(50))
"""
# Decorating Functions Accepting Arguments
"""def decorator(func):
    def wrapper(*args, **kwargs):
        print("Upper")
        func(*args, **kwargs)
        print("Down")

    return wrapper


@decorator
def chocolate():
    print("Chocolate")


@decorator
def cake(name):
    print(name + ' Cake')


chocolate()
cake('Apple')
"""
# Another Way Of Using Decorator
"""def decorator(func):
    def wrapper():
        print("Upper")
        func()
        print("Down")

    return wrapper


@decorator
def chocolate():
    print("Chocolate")


@decorator
def cake():
    print('Cake')


chocolate()
cake()"""
"""
# Decorators
def chocolate():
    print("Chocolate")


def decorator(func):
    def wrapper():
        print("Up")
        func()
        print("Down")

    return wrapper


chocolate = decorator(chocolate)

chocolate()
"""
"""
# Variable Length Keyword Arguments
def products(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + value)


products(name="phone", price="100")
products(name="tv stand", price="250", description="Description")
"""
""""
# Variable Length Positional Arguments
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4, 5))
"""""
"""
# Recursion In Python
def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


print(factorial(4))
"""
# factorial(4) => return 4 * factorial(4-1)
# factorial(3) => return 3 * factorial(3-1)
# factorial(2) => return 2 * factorial(2-1)
# factorial(1) => return 1


""""# EMI Calculator formula is: P x R x (1+R)^N / [(1+R)^N-1]
def emi_calculator(principal, rate, time):
    r = rate / 12 / 100
    emi = (principal * r * (1 + r) ** time) / ((1 + r) ** time - 1)
    return emi


print(emi_calculator(40000, 3.73, 240))
"""""
"""# Function To Check Palindrome

def check_palindrome(word):
    l = len(word)
    for i in range(l):
        if word[i] != word[l - i - 1]:
            return False
    return True


print(check_palindrome('pirriz'))
"""
"""
# Check If A String Is A Palindrome
word = 'run'
palindrome_state = True
word_length = len(word)
for i in range(word_length):
    if word[i] != word[word_length - i - 1]:
        palindrome_state = False
        break
    else:
        palindrome_state = True
if palindrome_state:
    print('This is THE palindrome')
else:
    print('This is NOT a palindrome')
"""
# Accessing Global Variables Inside A Function
"""count = 12


def increment():
    global count
    count += 1
    print(count)


increment()"""

# Local & Global Variables


# Returning List
"""#long version
def remove_duplicates(numbers):
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return new_list
"""

# short version
"""def remove_duplicates(numbers):
    return list(set(numbers))


myList = [1, 3, 5, 4, 56, 7, 86, 4, 9, 11, 21, 35, 22, 84, 83, 82, 25, 78, 53, 20, 11, 21]
result = remove_duplicates(myList)
print(sorted(result))
"""
# Passing List To A Function
"""def add(lista):
    total = 0
    for number in scores:
        # print(number)
        total += number
    return total


scores = [1, 2, 3, 4, 5]
result = add(scores)
print(result)
"""
"""
# Making A Function Return Multiple Values
pi = 3.14


def circle(r):
    area = pi * r * r
    circumference = pi * 2 * r
    return area, circumference


a, c = circle(10)
print(f'area is: {a}, circumference is: {c}')
"""
# nesting functions
"""def area(radius, pi=3.14):
    result = pi * radius * radius
    return result


def cost(circle_area, csm):
    total_cost = circle_area * csm
    return total_cost


print(cost(area(10, 3.15), 2))
"""
# funkcija return value

"""def area(radius, pi=3.14):
    result = pi * radius * radius
    return result


def cost(circle_area, csm):
    total_cost = circle_area * csm
    return total_cost


calculated_area = area(10, 3.15)
tc = cost(calculated_area, 2)
print(tc)"""

# default parameters
"""def area(radius, pi=3.14):
    print(pi * radius * radius)


area(10)
"""
# functions
"""def speed(distance, time):
    print(distance / time)


speed(distance=100, time=2)
"""
"""# creating a list of products, displaying cart items nicely
products = [
    {'name': 'Smartphone', 'price': 500, 'description': 'nice device'},
    {'name': 'Tablet', 'price': 1500, 'description': 'nice bigger device'},
    {'name': 'TV', 'price': 3500, 'description': 'device to watch sports'},
    {'name': 'Car', 'price': 23500, 'description': 'device get from a point to b point'}
]
cart = []
while True:
    choice = input('Continue shopping? ')
    if choice == 'yes':
        print('Here is the list of products to buy:')
        for index, product in enumerate(products):
            print(f'{index}: {product['name']} | {product['description']} | {product['price']} €')
        product_id = int(input('Enter ID of product you want to add to cart: '))

        # check if product is already in the cart
        if products[product_id] in cart:
            products[product_id]['quantity'] += 1
        else:
            products[product_id]['quantity'] = 1
            cart.append(products[product_id])

        print(f'Current cart content is ')
        for product in cart:
            print(
                f'{product['name']} | {product['price']} € | QTY: {product['quantity']} pcs')
            print(f'Total amount is: {product['price'] * product['quantity']}')
    else:
        break

print(f'Your content of cart is {cart}')
"""
"""
# adding items to cart using while loop
cart = []

while True:
    choice = input('Do you want to add item to cart? ')
    if choice == 'yes':
        item = input('Item to add: ')
        cart.append(item)
    else:
        break
print(cart)
"""
"""
# adding items to cart using for loop
cart = []

n = int(input('How many items you want to add to cart: '))
for x in range(n):
    item = input('Add item to cart: ')
    cart.append(item)
    print(cart)
"""
"""
# continue
counter = 0
while counter <= 10:
    counter += 1
    if counter == 5:
        continue
    print(counter)

"""
"""
# while loop with break
counter = 0

while counter <= 10:
    print(counter)
    if counter == 5:
        break
    counter += 1
"""
"""
# looping trough dictionary

people = {'John': 32, 'Rob': 40, 'Tim': 20}

for person in people:
    # print(person)
    print(people[person])

""""""
# looping trough list
fruits = ['Mango', 'Banana', 'Orange', 'Apple']

for item in fruits:
    print(item)
"""
"""
# FOR loop
for x in range(1, 11):
    print(x)
"""
"""
# range
# numbers = list(range(11))
# numbers = list(range(1, 11))
numbers = list(range(2, 102, 2))  # 3. broj je step

print(numbers)
"""
"""
# nested if
a = 6
b = 14

if a > 5:
    if b > 15:
        print('A is >5 & B je >15')
    else:
        print('B nije >15 ali a>5')
else:
    print('A nije > 5')
"""
"""
# add remove set
seta = {1, 2, 3, 4, 5}
# seta.discard(2)
# print(seta)
# seta.pop()
seta.clear()
print(seta)
"""
"""
# set operations
seta = {1, 2, 3, 4, 5}
setb = {4, 5, 6, 7, 8, 9}
print(seta | setb)
print(seta & setb)
print(seta - setb)
print(setb - seta)
print(setb ^ seta)
"""
"""
# set
number1 = set([1, 2, 3, 4, 5, 6])
number2 = {1, 3, 11, 2, 5, 6, 4}
emptySet = set()
print(number2)
print(type(emptySet))
"""
"""
# dictionary popout
prices = {'iphone': 400, 'ipad': 500, 'android': 600}
a = prices.pop('iphone')
print(prices)
"""
"""
# BMI = weight in kh / (height in m)^2

weight = float(input('Enter your weight in kg: '))
height = float(input('Enter your height in meters: '))

bmi = weight / height ** 2

print(f'Your BMI is {bmi}.')
"""

"""
firstname = input('Enter your first name: ')
lastname = input('Enter your last name: ')

username = firstname + ' ' + lastname
emailAddress = firstname + '.' + lastname + '@gmail.com'
print(f'Your username is: {username}')
print(f'Your email address is: {emailAddress.lower()}')
"""
"""'
# simple interest calculator
principal = int(input('Enter the amount of borrowed: '))
years = float(input('Enter the period in years: '))
rate = float(input('Enter the rate of interest: '))

interest = principal * years * rate / 100

print(f'Interest rate for {years} years is {rate}%')
"""
