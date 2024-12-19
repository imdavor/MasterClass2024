import tkinter as tk
from compressmodule import compress, decompress

window = tk.Tk()
window.title("Compression Engine")
window.geometry("600x400")


def compression(i, o):
    compress(i, o)


def decompression(i, o):
    decompress(i, o)


input_label = tk.Label(window, text="Input File To Compress/DeCompress")
output_label = tk.Label(window, text="Name of Compressed/DeCompressed File")

compress_button = tk.Button(
    window,
    text="Compress",
    command=lambda: compression(input_entry.get(), output_entry.get()),
)
compress_button.grid(row=2, column=1)

decompress_button = tk.Button(
    window,
    text="DeCompress",
    command=lambda: decompression(input_entry.get(), output_entry.get()),
)
decompress_button.grid(row=3, column=1)

input_entry = tk.Entry(window)
output_entry = tk.Entry(window)
input_label.grid(row=0, column=0)
input_entry.grid(row=0, column=1)
output_label.grid(row=1, column=0)
output_entry.grid(row=1, column=1)


window.mainloop()
