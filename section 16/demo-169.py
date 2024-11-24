# 169. Filtering Students
"""students = [
    {"name": "Alice", "age": 18, "grade": "A"},
    {"name": "Bob", "age": 17, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"},
    {"name": "David", "age": 16, "grade": "C"},
    {"name": "Eve", "age": 18, "grade": "A"}
]
a_students = list(filter(lambda s: s["age"] > 18 and s["grade"] == "A", students))
# lambda s: s = svaki entry u ovoj listi; s[] = s of...
print(a_students)"""

# 168. Filter Prime Numbers - diviszible by 1 or itself
"""numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(7))

primes_numbers = list(filter(is_prime, numbers))
print(primes_numbers)"""

# 166. Reversing a List Using Map.
"""def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sq = [0, 1]
        fib_sq.extend(map(lambda i: fib_sq[i - 1] + fib_sq[i - 2], range(2, n)))
        return fib_sq


fibonacci_sequence = fibonacci(10)
print(fibonacci_sequence)
"""
# 165. Extracting Initials Using Map
"""names = ["John Doe", "Alan Ford", "Bob Rock"]
initials = list(map(lambda name: "".join([n[0] for n in name.split()]), names))
print(initials)
"""
# 164. Extracting Initials From Name using split()
"""
for name in names:
    print(name.split()[0][0] + name.split()[1][0])
"""

# 163. Celsius to Fahrenheit Using Map
"""t_celsious = [0, 1, 25, 30, 15, 10, 35]

t_farenheight = list(map(lambda c: c * 9 / 5 + 32, t_celsious))

print(t_farenheight)
"""
"""# 162. Generators In Python - slicno listi ali se ne pospremaju u memoriju i slicno funkcijama
def even_generator(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(even_generator(100)))"""

"""def function(): counter = 0 while counter <= 10: # slicno kao i return ali: Naredba yield obustavlja izvršenje 
funkcije i šalje vrijednost natrag pozivatelju, ali zadržava # dovoljno stanja da omogući funkciji nastavak tamo gdje 
je stala. yield counter counter += 1


print(list(function()))"""

# 161. Filter In Python
"""numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ovo je booolen function
# def odd(x):
#     if x % 2 == 1:
#         return x


# odd_numbers = list(filter(odd, numbers))  # u filter ide funk + lista, onda sve u listu pa onda u varijablu 
odd_numbers = list(filter(lambda x: x % 2 == 1, numbers))  # ovak bi zgledalo da koristimo lambdu- onda nam ne treba 
funkcija print(odd_numbers)"""
"""" ovo je bez filtera
odd_nums = []
for number in numbers:
    if number % 2 == 1:
        odd_nums.append(number)
print(odd_nums)"""
"""# 160. Using Map In Different Ways

names = ['john', 'rob', 'mike']
# cap_names = list(map(str.capitalize, names))
cap_names = list(map(str.upper, names))
print(cap_names)
"""
"""prices = [100, 200, 300, 400, 500]
new_prices = list(map(lambda x: x - x * 5 / 100, prices))
print(new_prices)"""

"""numbers = ['1', '2', '3', '4', '5']

new_list = list(map(int, numbers)) #prebacujemo stringove u int, pa mapiramo pa konvertiramo u listu

print(new_list)"""

# 159. Map In Python - da ne zauzimamo memoriju sa loop
"""numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

new_list = list(map(square, numbers))  # mapiramo, prebacimo u listu, ubacimo u varijablu- čitaj unatrag
print(new_list)
"""
"""for number in numbers:
    print(square(number))
print(square(10))"""

# 158. Lambda Functions In Python
"""
def square(x):
    return x ** 2


print(square(5))

result = (lambda x: x ** 2)(5)
print(result)
result = (lambda x, y: x + y)(5, 2)
print(result)
result = (lambda x=10, y=20: x + y)(y=2)
print(result)
"""
