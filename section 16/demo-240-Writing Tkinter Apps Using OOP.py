from tkinter import *


class Demo:  # objekt klase Demo

    def __init__(self, rootone):  # definiramo konstruktor
        frame = Frame(rootone)  # kreira se frame, rootone je root
        frame.pack()  # frame se postavlja na root

        self.printbutton = Button(
            frame, text="Print Message", command=self.printmessage
        )
        self.quitbutton = Button(
            frame, text="Exit", command=frame.quit # ne moramo raditi funkciju quit, možemo koristiti quit()
        )
        self.printbutton.pack()  # button se postavlja na frame
        self.quitbutton.pack()  # button se postavlja na frame

    def printmessage(self):
        print("Clicked!")


root = Tk()  # kreira se root window
b = Demo(root)  # objekt klase Demo koji se proslijedi kao argument rootone

root.mainloop()  # mainloop
