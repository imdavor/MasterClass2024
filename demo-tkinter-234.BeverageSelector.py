# 234. Beverage Selector
from tkinter import *

# create window objekt
root = Tk()
root.geometry("300x300")

sugar_var = BooleanVar()
ice_var = BooleanVar()
cream_var = BooleanVar()


def selected():
    sugar = sugar_var.get()
    ice = ice_var.get()
    cream = cream_var.get()
    if sugar:
        sugar = "Sugar"
    else:
        sugar = "No sugar"
    if ice:
        ice = "Ice"
    else:
        ice = "No ice"
    if cream:
        cream = "Cream"
    else:
        cream = "No cream"

    label.config(
        text="Options selected are: \n" + str(sugar) + "\n " + str(ice) + "\n " + str(cream)
    )


sugar_checkbox = Checkbutton(root, text="Sugar", variable=sugar_var, command=selected)
ice_checkbox = Checkbutton(root, text="Ice", variable=ice_var, command=selected)
cream_checkbox = Checkbutton(root, text="Cream", variable=cream_var, command=selected)


sugar_checkbox.pack()
ice_checkbox.pack()
cream_checkbox.pack()

label = Label(root)
label.pack()


root.mainloop()
