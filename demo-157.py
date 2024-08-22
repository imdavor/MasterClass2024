#
# Coding challenge part 6
# 1. Write Python code to open a file named demo.txt and write some random data into it.
# 2. Open the file, read the contents and display them as output.
# 3. Write python code to add additional text to the existing file on a new line without deleting the previous contents.
# writing data to the file

# Solution
f = open('demo.txt', 'w')
f.write("hello there")
f.close()
# reading data from the file
f = open('demo.txt', 'r')
print(f.read())
f.close()
# adding additional contents
f = open('demo.txt', 'a')
f.write('\n Hello again')
f.close()

"""# 150. Preserving Old Data,
# 151. Reading User Data
# 152. Editing User Data
# 153. Deleting User Data
import json
import os.path


def save_user_data():
    user_list = []

    while True:
        name = input('Enter name (or q to quit: ')
        if name == 'q':
            break
        email = input('Enter email: ')
        contact = input('Enter contact: ')

        # create dictionary
        user_data = {
            "name": name,
            "email": email,
            "contact": contact
        }
        # save any user data
        user_list.append(user_data)

    if os.path.exists('user_data.json'):  # provjera da li file uopce postoji
        with open('user_data.json', 'r') as file:
            existing_data = json.load(file)  # uzima file i pretvara ga u dictionary
        user_list.extend(existing_data)  # existing_data dodajemo u user_list i nakon ovoga dodajemo nove podatke(dolje)

    with open('user_data.json', 'w') as file:
        json.dump(user_list, file)  # zabi json file u user_list
    print('User data saved successfully!')


def if_data_exist():
    if not os.path.exists('user_data.json'):
        print('No user data found')
        return


def read_user_data():
    # prvo provjeravamo da li file uopce postoji
    if not os.path.exists('user_data.json'):
        print('No user data found')
        return
    # open file
    with open('user_data.json', 'r') as file:
        user_list = json.load(file)  # pretvara u python listu i spremamo ga u varijablu
        for user_data in user_list:
            print('Name:', user_data['name'])
            print('Email:', user_data['email'])
            print('Contact:', user_data['contact'])
            print('\n')


def edit_user_data(name):
    if_data_exist()  # provjera da li file uopce postoji

    # otvaramo i spremamo podatke u user_list
    user_found = False  # postavka ako user ne postoji
    with open('user_data.json', 'r') as file:
        user_list = json.load(file)
    for user_data in user_list:
        if user_data['name'].lower() == name.lower():
            email = input('Enter updated email: ')
            contact = input('Enter updated contact: ')

            # update podataka iz gore dobivenog
            user_data['email'] = email
            user_data['contact'] = contact
            user_found = True
            break

    if not user_found:
        print('User doesnt exist')

    # Otvaramo file i zapisujemo nove podatke u njega - dump-amo user_list u file
    with open('user_data.json', 'w') as file:
        json.dump(user_list, file)
    print('User data updated successfully')


def delete_user_data(name):
    if_data_exist()  # provera da li file uopce postoji

    # otvaramo i spremamo podtke u user_list
    user_found = False  # postavka ako user ne postoji
    with open('user_data.json', 'r') as file:
        user_list = json.load(file)
    for user_data in user_list:
        if user_data['name'].lower() == name.lower():
            user_list.remove(user_data)
            user_found = True
            break

    if not user_found:
        print('User doesnt exist')

    # Otvaramo file i zapisujemo nove podatke u njega - dump-amo user_list u file
    with open('user_data.json', 'w') as file:
        json.dump(user_list, file)
    print('User data removed successfully')


delete_name = input('Enter name to delete: ')
delete_user_data(delete_name)
read_user_data()
# edit_name = input('Enter name to edit: ')
# edit_user_data(edit_name)

# save_user_data()
# read_user_data()
"""
"""# 149. Writing Serialised Data To File
import json


def save_user_data():
    user_list = []

    while True:
        name = input('Enter name (or q to quit: ')
        if name == 'q':
            break
        email = input('Enter email: ')
        contact = input('Enter contact: ')

        # create dictionary
        user_data = {
            "name": name,
            "email": email,
            "contact": contact
        }
        # save any user data
        user_list.append(user_data)

        with open('user_data.json', 'w') as file:
            json.dump(user_list, file)  # zabi json u user_list
        print('User data saved successfully!')


save_user_data()
"""
"""# 148. Deserialization
json_data = '{"name": "John Doe", "age": 30, "city": "New York"}'
data = json.loads(json_data)
print(data)
"""

"""# 147. Serialization

data = {"name": 'John Doe',
        'age': 30,
        'city': 'New York'}
json_data = json.dumps(data)  # konvertira podatke u json string
print(json_data)
"""
