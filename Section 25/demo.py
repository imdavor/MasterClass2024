from tkinter import *


window = Tk()
window.title("Invoice creator")

medicines = {"Medicine A": 10, "Medicine B": 20, "Medicine C": 30, "Medicine D": 40}


medicine_label = Label(window, text="Medicine: ")
medicine_label.pack()

medicine_listbox = Listbox(window, selectmode="single")
for medicine in medicines:
    medicine_listbox.insert(END, medicine)


medicine_listbox.pack()

quantity_label = Label(window, text="Quantity: ")
quantity_label.pack()
quantity_entry = Entry(window)
quantity_entry.pack()

add_button = Button(window, text="Add medicine: ")
add_button.pack()

total_amount_entry = label = Label(window, text="Total amount: ")
total_amount_entry.pack()

customer_label = Label(window, text="Customer name: ")
customer_label.pack()
customer_entry = Entry(window)
customer_entry.pack()

generate_button = Button(window, text="Generate Invoice")
generate_button.pack()


invoice_text = Text(window, height=10, width=50)
invoice_text.pack()

window.mainloop()
