# creating a list of products, displaying cart items nicely
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
        cart.append(products[product_id])
        print(f'Current cart content is ')
        for product in cart:
            print(f'{product['name']} | {product['price']} €')
    else:
        break

print(f'Your content of cart is {cart}')

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
