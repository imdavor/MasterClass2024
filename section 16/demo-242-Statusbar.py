from tkinter import *

def function1():
    print("Printamo sadržaj iz function1!")

# create window objekt
root = Tk()
root.geometry("300x300")

# create menu objekt, ovo je općenito cijeli "prozor"
mymenu = Menu(root)

root.config(menu=mymenu) # postavi ovaj mymenu kao glavni menu u root windowu
submenu = Menu(mymenu)# kreiramo submenu tj menu koji ide u mymenu

mymenu.add_cascade(label="File", menu=submenu) # u submenu dodajemo File, glavni menu

submenu.add_command(label="New", command=function1) # ovaj dodajemo u File grupu
submenu.add_command(label="Open") # ovaj dodajemo u File grupu
submenu.add_command(label="Exit", command=root.quit) # ovaj dodajemo u File grupu

# create statusbar
statusbar = Label(root, text="Statusbar", bd=1, relief=SUNKEN, anchor=W) # napravimo statusbar u rootu border 1 relief SUNKEN anchor W
statusbar.pack(side=BOTTOM, fill=X) # statusbar se postavlja na root prozor u BOTTOM i u X osi  



root.mainloop()
