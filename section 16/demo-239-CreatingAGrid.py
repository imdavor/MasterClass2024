from tkinter import *

root = Tk()


# želim kreirati 9 buttona i postaviti ih u grid sa for loopom
# svaki loop će se izvrtjeti 3 puta, prvo unutarnji loop pa vanjski
for x in range(3):
    for y in range(3):
        frame = Frame(root)
        frame.grid(row=x, column=y)
        button = Button(frame, text=f"Button {x} \nColumn {y}")
        button.pack(padx=5, pady=5)


root.mainloop()
