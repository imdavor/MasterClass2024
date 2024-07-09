from tkinter import *
from PIL import ImageTk

window = Tk()

window.geometry('1280x700')

window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='images/bg.jpg')

bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

loginFrame = Frame(window, bg='white')
loginFrame.place(x=400, y=150)

logoImage = PhotoImage(file='images/logo.png')  # importing image
usernameImage = PhotoImage(file='images/user.png')  # importing image
passwordImage = PhotoImage(file='images/password.png')  # importing image

logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

usernameLabel = Label(loginFrame, image=usernameImage, text='Username', compound=LEFT, font=('Helvetica', 20),
                      bg='white')
usernameLabel.grid(row=1, column=0, pady=10, padx=20)
usernameEntry = Entry(loginFrame, font=('Helvetica', 20), bd=5, fg='royalblue')
usernameEntry.grid(row=1, column=1, pady=10, padx=20)

passwordLabel = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT, font=('Helvetica', 20),
                      bg='white')
passwordLabel.grid(row=2, column=0, pady=10, padx=20)
passwordEntry = Entry(loginFrame, font=('Helvetica', 20), bd=5, fg='royalblue')
passwordEntry.grid(row=2, column=1, pady=10, padx=20)

loginButton = Button(loginFrame, text='Login', font=('Helvetica', 14), width=15, fg='white', bg='cornflower blue',
                     cursor='hand2')
loginButton.grid(row=3, column=1)

window.mainloop()
