from tkinter import *
from PIL import ImageTk

window = Tk()

window.geometry('1280x700')

window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=50, y=50)

loginFrame = Frame(window)

window.mainloop()
