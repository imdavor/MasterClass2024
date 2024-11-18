from tkinter import *


# create window objekt
root = Tk()
# create display
display = Entry(root)
# root.geometry("200x200")
display.grid(row=1, columnspan=6)

i=0 # postavljamo index na 0
def get_number(num):
    global i
    display.insert(i, num) # index(pozicija broja u displayu) broja je i, proslijedi num u display
    i+=1 # svaki put kada je dodan broj povećaj poziciju indexa za 1

def get_operation(operator):
    global i # globalni i koji će dati poziciju operatora nakon gore odabranog broja
    length = len(operator) # uzmi duljinu operatora jer ima nekih koji imaju više od 1 znaka
    display.insert(i, operator) # dodaj operator na poziciju u displpay
    i+=length # povećaj poziciju indexa za duljinu operatora


# kako bi se brojevi prikazali u displayu izrađujemo array sa brojevima od 1-9 tako da funkcija get_number() može biti pozvana za svaki broj koji je kliknut
numbers = [1,2,3,4,5,6,7,8,9]
counter = 0 #postavljamo counter na 0 jer želimo da se brojevi prikazuju od 0-9
# dodajmo 3x3 grid i buttone
for x in range(3):
    for y in range(3):
        button_text = numbers[counter] # svaki button loop kroz numbers
        button= Button(root, text=button_text, width=4,height=2, command=lambda text=button_text:get_number(text)) #counter=brojevi od 0-9; ubacujemo lambda 
        button.grid(row=x+2, column=y) # kreiraj grid, x+2 koji će početi u 2.redu jer je 1. red rezerviran za display
        counter += 1 

#button nula
buttonzero= Button(root, text="0", width=4, height=2, command=lambda :get_number(0))
buttonzero.grid(row=5, column=1)

# kreiramo listu operacija koje će raditi
operations = ["+", "-", "*", "/", "*3.14", "%","(","**",")","**2"]
# 10 operacija pa kreiramo buttone za svaku operaciju
count=0
for x in range(4):
    for y in range(3): #loopamo 12 puta ali iza ograničavamo dužinom liste
        if count<len(operations): # ako je dužina liste manje od 10 kreiraj buttone
            button= Button(root, text=operations[count], width=4, height=2, command=lambda text=operations[count]:get_operation(text)) # u buttone stavi tekst iz liste
            # dodaj lambda funkciju u koju će se uglaviti znak iz arraya i u get_operation() pozvati tu text varijablu
            count += 1
            button.grid(row=x+2, column=y+3) # napravi grid od 2. reda ali počni sa kolumnom 3



root.mainloop()
