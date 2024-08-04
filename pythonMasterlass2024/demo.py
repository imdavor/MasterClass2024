# break
counter = 1
while counter <= 10:
    print(counter)
    if counter == 5:
        break
    counter += 1

"""
# while loop
counter = 1
while counter <= 10:
    print(counter)
    counter += 1

"""
# nested if

"""# elif
marks = int(input('Unesi bodove: '))

if marks >= 90:
    print('Ocjena 5')
elif marks >= 80:
    print('Ocjena 4')
elif marks >= 70:
    print('Ocjena 3')
elif marks >= 50:
    print('Ocjena 2')
else:
    print('Ocjena 1')"""

"""#  if
age_input = int(input('Enter your age: '))

if age_input > 18:
    print('You are adult')
else:
    print('You are NOT adult')
"""
"""
# Coding Challenge 2

fav_food = ['apple', 'mayo', 'peach', 'milk', 'bread']
print(fav_food[2])
fav_food.append('coffee')
print(fav_food)
# insert an element named tacos at the 3rd index position of the list and print out the list elements.
index = fav_food.index('peach')
fav_food.insert(index + 1, 'taco')
print(fav_food)"""

"""
products = {'phone': 100, 'Tablet': 200, 'Laptop': 300, 'journal': 40}


print(products)"""
"""
# change value in dictionary
product_price_change = input('Enter product that you want to change price: ')
price_change = input('Enter new price: ')
products[product_price_change] = price_change
print(f'New price for {product_price_change} is {price_change} ')
print(products)
"""
"""
# delete products from dictionary
delete_product = input('Enter product that you want to delete: ')
del products[delete_product]
print(products)
"""
"""product = input('Enter product to check the price: ')
print(f'Price of {product} is {products[product]}')"""
"""
new_product = input('Enter a new product to add: ')
new_product_price = int(input('Enter a new product price: '))
products[new_product] = new_product_price
print(f'Added {new_product} with price {new_product_price} to a list. ew list {products}')
"""
"""
# adding items top position in list
products = ['phone', 'Tablet', 'Laptop', 'journal']
print(f'Current list of items: {products}')

add_item = input('Add item to list: ')
add_after = input(f'After which product yoo want to place {products}: ')
index = products.index(add_after)
products.insert(index + 1, add_item)
print(f'Current list of items: {products}')

"""
"""
# removing-adding items from list
products = ['phone', 'Tablet', 'Laptop', 'journal']
print(f'Current list of items: {products}')

remove_item = input('Remove item from list: ')
products.remove(remove_item)
print(f'Current list of items: {products}')

add_item = input('Add item to list: ')
products.append(add_item)
print(f'Current list of items: {products}')
"""

"""
# search item
products = ['phone', 'Tablet', 'Laptop', 'journal']
item = input('Find product in list: ')
print(item in products)
"""
