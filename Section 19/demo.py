from gtts import gTTS
import os
from tkinter import *


# 292. Converting User Input To Speech


def TextToSpeech():
    text = entry.get()
    lang = "en"
    output = gTTS(text=text, lang=lang, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")


root = Tk()  # create a main window
canvas = Canvas(root, width=400, height=300)  # create a canvas for main window
canvas.pack()


entry = Entry(root)  # create a entry for main window
canvas.create_window(200, 180, window=entry)  # create a window for entry

button = Button(root, text="Convert", command=lambda: TextToSpeech())
canvas.create_window(200, 230, window=button)  # create a window for button
button_close = Button(root, text="Close", command=root.destroy)
canvas.create_window(200, 260, window=button_close)

root.mainloop()


### Converting file data to audio ###

# text = open("demo.txt", "r").read()
# lang = "en"
# output = gTTS(text=text, lang=lang, slow=False)
# output.save("output.mp3")

# os.system("start output.mp3")


### Convert text to speech ###

# text = "Hello, how are you?"
# output = gTTS(text=text, lang="en", slow=False)
# output.save("output.mp3")

# os.system("start output.mp3")
