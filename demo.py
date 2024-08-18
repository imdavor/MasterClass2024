# Try & except block
n = int(input('Enter numerator: '))
d = int(input('Enter denominator: '))
result = 0
try:
    result = n / d
    print(result)
except ZeroDivisionError:
    print(f'Cant divide by zero.Result is {result}.')

# Syntax error
