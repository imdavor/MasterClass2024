# Coding challenge part 5
# # Write a function which would divide two numbers, design the function in a manner that it handles the divide by zero exception.

def divide():
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    try:
        return a / b
    except ZeroDivisionError:
        print('Cant divide by zero')
        return 0


# print(divide(8, 0))
print(divide())

# Solution to coding challenge 5
#
# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print("There is a divide by zero error")
#         return 0
#
# x = float(input('Enter a number'))
# y = float(input('Enter value by which you want to divide the number'))
# result = divide(x, y)
# print(result)


"""# Try & except & Else & Finally block
n = int(input('Enter numerator: '))
d = int(input('Enter denominator: '))
result = 0
try:
    result = n / d
    print(result)
except ZeroDivisionError:
    print(f'Cant divide by zero.')
else:
    print(result)
finally:
    print('This code will be executed no matter what')
# Syntax error"""
