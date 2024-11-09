# 234. Beverage Selector
from tkinter import *

# create window objekt
root = Tk()
root.geometry("300x300")

root.mainloop()


# 233. Checkboxes
"""from tkinter import *

# create window objekt
root = Tk()
root.geometry("300x300")


def selected():
    display_label.config(text=check_value.get())


check_value = BooleanVar()
checkButton = Checkbutton(root, text="Check me", variable=check_value, command=selected)
checkButton.pack()

display_label = Label(root)
display_label.pack()


root.mainloop()"""


# 232. Adding Two Numbers
""""from tkinter import *


def add():
    n1 = int(number1.get())
    n2 = int(number2.get())
    result = str(n1 + n2)
    display_label.config(text="Rezultat je: " + result)


# create window objekt
root = Tk()
root.geometry("300x300")


number1 = Entry(root)
number2 = Entry(root)
number1.pack()
number2.pack()

button = Button(root, text="Zbroji", command=add)
button.pack()

display_label = Label(root)
display_label.pack()


root.mainloop()"""


# 230. Buttons
"""from tkinter import *


def display():
    # kako pokupimo upisane podatke iz entry boxa
    data = entry.get()
    print(data)


# create window objekt
root = Tk()
root.geometry("300x300")

# input box widget
entry = Entry(root)
entry.pack()


button = Button(root, text="Click me!", command=display)
button.pack()
root.mainloop()"""


# 229.Understanding Tkinter Widgets
"""from tkinter import *

# create window objekt
root = Tk()  # 1. kreirali smo objekt(zagrade) root(window) iz klase Tk()

# 3. možemo odrediti i veličinu prozora
root.geometry("300x300")
# 2. sada idemo koristiti widgete -- npr. label
hello = Label(
    root, text="Hello World!", fg="red", bg="white",font=("Arial", 16)
)  # želim da se Label pojavi u root windowu
hello.pack()  # sada actually prikazujemo text labela na prozoru

root.mainloop()  # 1. window se pojavi i postoji dok ga ne zatvorimo"""

""" Default 
from tkinter import *

# create window objekt
root = Tk()
root.geometry("300x300")

root.mainloop()

"""
