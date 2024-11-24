from tkinter import *
import ast # modul za konverziju iz stringa 

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

def clear_all():
    display.delete(0,END) # očisti sve od indexa (0) do (END) kraja

def calculate():
    entire_string = display.get()
    try:
        # ovo radi ast module, uzima string, evaluira i sprema u result
        node = ast.parse(entire_string, mode="eval")
        result =  eval(compile(node,'<string>', 'eval'))
        #  čistimo display i upisujemo result
        clear_all()
        display.insert(0, result)
    except: 
        clear_all()
        display.insert(0, "Something went worng") # ovaj try ako baci error na mjesto indexa 0 ubaci poruku Error

def undo():
    entire_string = display.get()
    if len(entire_string): # ako nije prazan display
        new_string = entire_string[:-1] #kreiraj novi string sa oduzetim zadnjim znakom iz displaya
        clear_all() # očisti display
        display.insert(0, new_string) # prikaži novi string u displayu
    else: # ako je u displayu 0 ne koristi undo
        clear_all() # očisti sve
        display.insert(0, "") # i baci prazan string na poziciju indexa 0


# kako bi se brojevi prikazali u displayu izrađujemo array sa brojevima od 1-9 tako da funkcija get_number() može biti pozvana za svaki broj koji je kliknut
numbers = [1,2,3,4,5,6,7,8,9]
counter = 0 #postavljamo counter na 0 jer želimo da se brojevi prikazuju od 0-9
# dodajmo 3x3 grid i buttone
for x in range(3):
    for y in range(3):
        button_text = numbers[counter] # svaki button loop kroz numbers
        button= Button(root, text=button_text, width=4,height=2, padx=3, pady=3, command=lambda text=button_text:get_number(text)) #counter=brojevi od 0-9; ubacujemo lambda 
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
            button= Button(root, text=operations[count], width=4, height=2, padx=3, pady=3,command=lambda text=operations[count]:get_operation(text)) # u buttone stavi tekst iz liste
            # dodaj lambda funkciju u koju će se uglaviti znak iz arraya i u get_operation() pozvati tu text varijablu
            count += 1
            button.grid(row=x+2, column=y+3) # napravi grid od 2. reda ali počni sa kolumnom 3

# dodajemo Clea
Button(root, text="AC", width=4, height=2, padx=3, pady=3,command=clear_all).grid(row=5, column=0)

#  i Jednako button
Button(root, text=" = ", width=4, height=2, padx=3, pady=3, command=calculate).grid(row=5, column=2)
Button(root, text=" Del ", width=4, height=2, padx=3, pady=3, command=lambda :undo()).grid(row=5, column=4)

root.mainloop()
