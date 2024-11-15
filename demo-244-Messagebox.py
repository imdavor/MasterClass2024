from tkinter import *
import tkinter.messagebox

# create window objekt
root = Tk()
root.geometry("300x300")

# tkinter.messagebox.showinfo("Info", "This is a message box!", icon="info")
response= tkinter.messagebox.askquestion("Question", "Do you like Python?", icon="question")
if response == "yes":
    print("You like Python!")
else:
    print("You don't like Python!")


root.mainloop()
