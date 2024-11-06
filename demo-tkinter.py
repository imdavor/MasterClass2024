# Tkinter
from tkinter import *

# create window objekt
root = Tk()  # 1. kreirali smo objekt(zagrade) root(window) iz klase Tk()

# 3. možemo odrediti i veličinu prozora
root.geometry("300x300")
# 2. sada idemo koristiti widgete -- npr. label
hello = Label(root, text="Hello World!")  # želim da se Label pojavi u root windowu
hello.pack()  # sada actually prikazujemo text labela na prozoru

root.mainloop()  # 1. window se pojavi i postoji dok ga ne zatvorimo
