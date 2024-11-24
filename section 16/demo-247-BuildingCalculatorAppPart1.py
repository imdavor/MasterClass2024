from tkinter import *


# create window objekt
root = Tk()
# create display
display = Entry(root)
root.geometry("200x200")
display.grid(row=1, columnspan=6)

counter = 1
# dodajmo 3x3 grid i buttone
for x in range(3):
    for y in range(3):
        button= Button(root, text=counter, width=4,height=2) #counter=brojevi od 0-9
        button.grid(row=x+2, column=y) # kreiraj grid, x+2 koji će početi u 2.redu jer je 1. red rezerviran za display
        counter += 1 

#b utton nula
buttonzero= Button(root, text="0", width=4, height=2)
buttonzero.grid(row=5, column=1)

root.mainloop()
