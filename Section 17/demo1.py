from tkinter import *


root = Tk()
root.title("Student Management System")


frame = LabelFrame(root, text="Student Data")
frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

Label(frame, text="Name:").grid(
    row=0, column=0, padx=2, sticky="w"
)  # stavi label Name u grid i poravnaj na lijevo
name_entry = Entry(frame)
name_entry.grid(row=0, column=1, pady=2, sticky="we")

Label(frame, text="Address:").grid(
    row=1, column=0, padx=2, sticky="w"
)  # stavi label Address u grid i poravnaj na lijevo
address_entry = Entry(frame)
address_entry.grid(row=1, column=1, pady=2, sticky="we")

Label(frame, text="Age:").grid(
    row=2, column=0, padx=2, sticky="w"
)  # stavi label Address u grid i poravnaj na lijevo
age_entry = Entry(frame)
age_entry.grid(row=2, column=1, pady=2, sticky="we")

Label(frame, text="Phone number:").grid(
    row=3, column=0, padx=2, sticky="w"
)  # stavi label Address u grid i poravnaj na lijevo
number_entry = Entry(frame)
number_entry.grid(row=3, column=1, pady=2, sticky="we")

button_frame = Frame(root)
button_frame.grid(row=1, column=0, pady=5, sticky="ew")
Button(button_frame, text="Create table").grid(row=0, column=0, padx=5)
Button(button_frame, text="Add data").grid(row=0, column=1, padx=5)
Button(button_frame, text="Update data").grid(row=0, column=2, padx=5)
Button(button_frame, text="Delete data").grid(row=0, column=3, padx=5)

root.mainloop()
