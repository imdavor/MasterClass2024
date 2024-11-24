from tkinter import *

def function1():
    print("Printamo function1!")

# create window objekt
root = Tk()
root.geometry("300x300")

# create menu objekt, ovo je općenito cijeli "prozor"
mymenu = Menu(root)

root.config(menu=mymenu) # postavi ovaj mymenu kao glavni menu u root windowu
submenu = Menu(mymenu)# kreiramo submenu tj menu koji ide u mymenu
submenu_edit=Menu(mymenu) # kreiramo submenu tj menu koji ide u mymenu

mymenu.add_cascade(label="File", menu=submenu) # u submenu dodajemo File, glavni menu
mymenu.add_cascade(label="Edit", menu=submenu_edit) # dodajemo Edit u glavni submenu

submenu.add_command(label="New", command=function1) # ovaj dodajemo u File grupu
submenu.add_command(label="Open") # ovaj dodajemo u File grupu
submenu.add_command(label="Save") # ovaj dodajemo u File grupu
submenu.add_command(label="Exit", command=root.quit) # ovaj dodajemo u File grupu

submenu_edit.add_command(label="Cut") # ovaj dodajemo u Edit grupu
submenu_edit.add_command(label="Copy") # ovaj dodajemo u Edit grupu
submenu_edit.add_command(label="Paste") # ovaj dodajemo u Edit grupu


root.mainloop()
