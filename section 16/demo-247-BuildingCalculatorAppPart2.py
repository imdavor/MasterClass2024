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

#button nula
buttonzero= Button(root, text="0", width=4, height=2)
buttonzero.grid(row=5, column=1)

# kreiramo listu operacija koje će raditi
operations = ["+", "-", "*", "/", "*3.14", "%","(","**",")","**2"]
# 10 operacija pa kreiramo buttone za svaku operaciju
count=0
for x in range(4):
    for y in range(3): #loopamo 12 puta ali iza ograničavamo dužinom liste
        if count<len(operations): # ako je dužina liste manje od 10 kreiraj buttone
            button= Button(root, text=operations[count], width=4, height=2) # u buttone stavi tekst iz liste
            count += 1
            button.grid(row=x+2, column=y+3) # napravi grid od 2. reda ali počni sa kolumnom 3



root.mainloop()
