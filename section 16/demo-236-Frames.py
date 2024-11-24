# Frames and properties
from tkinter import *


# create window objekt
root = Tk()

frame1 = Frame(
    root, highlightthickness=1, highlightbackground="black", padx=10, pady=10
)
frame1.pack()

frame2 = Frame(root)
frame2.pack(side=BOTTOM)

button1 = Button(frame1, text="Button 1")
button2 = Button(frame2, text="Button 2")
button1.pack()
button2.pack()


root.geometry("300x300")


root.mainloop()
