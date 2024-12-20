import tkinter as tk
from compressmodule import compress, decompress
from tkinter import filedialog


def compression(i, o):
    compress(i, o)


def decompression(i, o):
    decompress(i, o)


def open_file():
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select a File to compress"
    )
    return filename


window = tk.Tk()
window.title("Compression Engine")
window.geometry("600x400")


compress_button = tk.Button(
    window,
    text="Compress",
    command=lambda: compression(open_file(), "compressed-ot.txt"),
)

decompress_button = tk.Button(
    window,
    text="DeCompress",
    command=lambda: decompression(open_file(), "de-compressed-ot.txt"),
)
compress_button.grid(row=2, column=1)
decompress_button.grid(row=2, column=2)


window.mainloop()
