from tkinter import *
import ast  # apstract syntax tree, pass any expression - sam kuži kaj treba napraviti


root = Tk()
root.title("Calculator")


# pišemo funkcije za operacije
# kad kliknemo gumb pokaže se broj i poveća se broj pozicije za slijedeći
i = 0  # pozicija nula


def get_number(num):
    global i
    display.insert(i, num)
    i += 1


def get_operation(operator):
    global i  # pozicija 0
    length = len(operator)  # uzimamo dužinu znakova operacije
    display.insert(i, operator)  # ubacujemo na poziciju znak
    i += 1  # dižemo poziciju za 1


def clear_all():
    display.delete(0, END)


def calculate():
    entire_string = display.get()  # 1. pokupi sve kaj je upisano u prozoru
    try:
        node = ast.parse(entire_string, mode="eval")  # stavi u var node
        result = eval(
            compile(node, "<string>", "eval")
        )  # 2. proslijedi upisano(node) u ast i evaluiraj string i stavi sve u var result
        clear_all()  # 3. očisti display
        display.insert(
            0, result
        )  # 4. ubaci evaluirani result u display na poziciju index 0
    except Exception:
        clear_all()
        display.insert(0, "Error")


def undo():
    entire_string = display.get()
    if len(entire_string):  # provjera da display nije prazan
        new_string = entire_string[
            :-1
        ]  # koristimo list slicing koristeći negative indexing
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "")


# dodajemo display za unos u prvi red
display = Entry(root, font=("default", 20))
display.grid(row=1, columnspan=6)

# dodajemo gumbe sa brojevima
# da bi get_number pokazao broj (button_text) u displayu koristimo array
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0
for x in range(3):
    for y in range(3):
        button_text = numbers[counter]
        button = Button(
            root,
            text=button_text,
            width=5,
            height=2,
            command=lambda text=button_text: get_number(text),
        )
        button.grid(row=x + 2, column=y, padx=1, pady=1)
        counter += 1

# dodajemo gumb za 0
button = Button(root, text=0, width=5, height=2, command=lambda: get_number(0))
button.grid(row=5, column=1, padx=1, pady=1)

# dodajemo gumbe za operacije
count = 0
operations = ["+", "-", "*", "/", "*3.14", "%", "(", "**", ")", "**2"]
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(
                root,
                text=operations[count],
                width=5,
                height=2,
                command=lambda text=operations[count]: get_operation(
                    text
                ),  # preko lambde stavramo parametar text i pozivamo funkciju
            )
            button.grid(row=x + 2, column=y + 3, padx=1, pady=1)
            count += 1


# dodajemo clear button u grid
Button(root, text="AC", width=5, height=2, command=clear_all).grid(
    row=5, column=0, padx=1, pady=1
)

# gumb izračunaj
Button(root, text=" = ", width=5, height=2, command=calculate).grid(
    row=5, column=2, padx=1, pady=1
)

# dodajemo gumb koji briše samo jednu znamenkuu unazad
# ideja je uzeti cijeli string, izbristi iz displaya, maknuti zadnju znameku i vratiti smanjeni string u display
Button(root, text=" <- ", width=5, height=2, command=lambda: undo()).grid(
    row=5, column=5, padx=1, pady=1
)


root.mainloop()
