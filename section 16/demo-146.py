# 147. Serialization


# 146. Saving Complex Data
def save_user_data():
    name = input('Enter a name: ')
    email = input('Enter an email: ')
    contact = input('Enter an contact: ')
    user_data = f'Name: {name}\nEmail: {email}\nContact: {contact}\n'
    with open('user_data.txt', 'a') as file:
        file.write(user_data)


def read_user_data():
    with open('user_data.txt', 'r') as file:
        print(file.read())


save_user_data()
read_user_data()

"""# 144. Saving User Data In A
while True:
    with open('names.txt', 'a') as file:
        name = input('Enter a name to be added: ')
        file.write(name + '\n')
        choice = input('Add another (y/n)?: ')
        if choice == 'n':
            break
# 145. Reading Saved Names
with open('names.txt', 'r') as file:
    #     names = file.read()
    # print(names)
    lines = file.readlines()
for line in lines:
    print(line.strip().capitalize())"""

"""# 143. Strip Method
with open('data.txt', 'r') as file:
    lines = file.readlines()

print(lines)
for line in lines:
    print(line.strip())
"""
"""# 142. Readline & Readlines
with open('data.txt', 'r') as file:
    # line1 = file.readline()
    # line2 = file.readline()
    lines = file.readlines()

print(lines)
for line in lines:
    print(line)
"""
"""# 141. Opening Files Using With
with open('data.txt', 'r') as file:
    contents = file.read()
    print(contents)"""

"""# 140. Writing & Appending Data To A File
file = open('data.txt', 'w')
file.write('Novi sadrzaj u fileu')
file.close()
"""
#
"""# Opening A File
file = open('data.txt', 'r')
# 139. Reading Data From A File
# content = file.read()
content = file.readline()
print(content)
file.close()
"""
