# 149. Writing Serialised Data To File
import json


def save_user_data():
    user_list = []

    while True:
        name = input('Enter name (or q to quit: ')
        if name == 'q':
            break
        email = input('Enter email: ')
        contact = input('Enter contact: ')

        # creatind dictionary
        user_data = {
            "name": name,
            "email": email,
            "contact": contact
        }
        # save any user data
        user_list.append(user_data)

        with open('user_data.json', 'w') as file:
            json.dump(user_list, file)  # zabi json u user_list
        print('User data saved succesfully')


save_user_data()

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
