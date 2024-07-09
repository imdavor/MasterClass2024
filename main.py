from tkinter import *
from PIL import ImageTk

window = Tk()

window.geometry('1280x700')

window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

loginFrame = Frame(window)

window.mainloop()
