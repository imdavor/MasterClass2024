import bcrypt

password = b"thisismypassword" # to byte
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

# entered_password = input("Enter password to login: ")
# entered_password = bytes(entered_password, 'utf-8')
# if bcrypt.checkpw(entered_password, hashed):
#     print("Login successful")
# else:
#     print("Login failed")
