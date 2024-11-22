from tkinter import *


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


# dodajemo display za unos u prvi red
display = Entry(root)
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


root.mainloop()
