from tkinter import *
import bcrypt


root=Tk()
root.geometry("300x300")
root.title("Login")

def validate(password):
    hash= b'$2b$12$GjSmRKOYRxvc8rET7ctkMulZzuMoMwBN/PGUVL7gt2Dr8L9XOkVry'
    password= bytes(password, 'utf-8')
    if bcrypt.checkpw(password, hash):
        print('Login successful!')
    else:
        print('Invalid password!')


# dodaj entry za upisivanje passwoorda
password_entry = Entry()
password_entry.pack()
password_entry.get()

button= Button(root, text="Validate password", command=lambda:validate(password_entry.get())) 
button.pack()

# prikaži poruku nakon validacije
message_label = Label(root, text="")
message_label.pack()

def display_message(is_valid):
    message = "Login successful!" if is_valid else "Invalid password!"
    message_label.config(text=message)

# Update button command to display message
button = Button(root, text="Validate password", command=lambda: display_message(validate(password_entry.get())))
button.pack()

root.mainloop()
