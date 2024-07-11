from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import time


def clock():
    currentdate = time.strftime('%d.%m.%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'Date: {currentdate}\nTime: {currenttime}')
    datetimeLabel.after(1000, clock)


count = 0
text = ''


def slider():
    global text, count  # nemožemo mijenjati varijablu unutar funkcije pa je stavljamo u global(scope)
    text += text + s[count]
    sliderlabel.config(text=text)
    count += 1
    sliderlabel.after(1000, slider)


root = Tk()
root.geometry('1280x700')
root.title('Student Management System')
root.resizable(False, False)

datetimeLabel = Label(root, text='hello', font=('Helvetica', 18, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()

s = 'Student management System'
sliderlabel = Label(root, text=s, font=('Helvetica', 28, 'bold'))
sliderlabel.place(x=200, y=0)
slider()

root.mainloop()
