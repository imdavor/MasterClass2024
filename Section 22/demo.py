# install pycube
# install moviepy

from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Video Downloader")
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# widget for entry to accept video url
# app label
app_label = Label(root, text="Video Downloader", fg="blue", font=("Arial", 20))
canvas.create_window(200, 20, window=app_label)


url_label = Label(root, text="Enter video URL:")
url_entry = Entry(root)
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)


# widget for path  to download video
path_label = Label(root, text="Select folder to download:")
path_button = Button(root, text="Select")
canvas.create_window(200, 140, window=path_label)
canvas.create_window(200, 160, window=path_button)


root.mainloop()
