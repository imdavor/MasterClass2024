from tkinter import *
from tkinter import ttk
import psycopg2
from tkinter import messagebox


# dodajemo koneciju na bazu  koja se ponavlja
def run_query(query, params=()):  # u formi tuplea params=()

    conn = psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432",
    )
    cur = conn.cursor()
    query_result = None
    try:
        cur.execute(query, params)
        if query.lower().startswith("select"):
            query_result = cur.fetchall()
        conn.commit()
    except psycopg2.Error as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        cur.close()
        conn.close()
    return query_result


# kad god otvorimo program, refresha se view podataka
def refresh_treeview():
    # brisemo sve podatke iz treeview-a da se slučajno ne ponavljaju
    for item in tree.get_children():
        tree.delete(item)
    # dodajemo podatke u treeview
    records = run_query("SELECT * FROM students ORDER BY students_id ASC")
    for record in records:
        tree.insert("", END, values=record)


# insert data funkcija
def insert_data():
    query = "INSERT INTO students(name, address, age, number) VALUES (%s,%s,%s,%s)"
    parameters = (
        name_entry.get(),
        address_entry.get(),
        age_entry.get(),
        number_entry.get(),
    )
    run_query(query, parameters)
    messagebox.showinfo("Success!", "Student added successfully!")
    refresh_treeview()


def delete_data():
    selected_item = tree.selection()[0]
    student_id = tree.item(selected_item)["values"][0]
    query = "DELETE FROM students WHERE students_id = %s"
    parameters = (student_id,)
    run_query(query, parameters)
    refresh_treeview()
    messagebox.showinfo("Success!", "Student deleted successfully!")


# kad korisnik klikne na update, treba da se popune polja za update


# update data funkcija
def update_data():
    selected_item = tree.selection()[0]
    student_id = tree.item(selected_item)["values"][0]

    query = "UPDATE students SET name=%s, address=%s, age=%s, number=%s WHERE students_id = %s"
    parameters = (
        name_entry.get(),
        address_entry.get(),
        age_entry.get(),
        number_entry.get(),
        student_id,
    )
    run_query(query, parameters)
    messagebox.showinfo("Success!", "Student updated successfully!")
    refresh_treeview()


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS students (
        students_id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        address VARCHAR(100),
        age INTEGER,
        number VARCHAR(20)
    )
    """
    run_query(query)
    messagebox.showinfo("Success!", "Table created successfully!")
    refresh_treeview()


# 274. Creating Tkinter Window
root = Tk()
root.title("Student Management System")


frame = LabelFrame(root, text="Student Data")
frame.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

Label(frame, text="Name:").grid(
    row=0, column=0, padx=2, sticky="w"
)  # stavi label Name u grid i poravnaj na lijevo
name_entry = Entry(frame)
name_entry.grid(row=0, column=1, pady=2, sticky="we")

Label(frame, text="Address:").grid(row=1, column=0, padx=2, sticky="w")
address_entry = Entry(frame)
address_entry.grid(row=1, column=1, pady=2, sticky="we")

Label(frame, text="Age:").grid(row=2, column=0, padx=2, sticky="w")
age_entry = Entry(frame)
age_entry.grid(row=2, column=1, pady=2, sticky="we")

Label(frame, text="Phone number:").grid(row=3, column=0, padx=2, sticky="w")
number_entry = Entry(frame)
number_entry.grid(row=3, column=1, pady=2, sticky="we")


# 275. Adding Buttons
button_frame = Frame(root)
button_frame.grid(row=1, column=0, pady=5, sticky="ew")
Button(button_frame, text="Create table", command=create_table).grid(
    row=0, column=0, padx=5
)
Button(button_frame, text="Add data", command=insert_data).grid(row=0, column=1, padx=5)
Button(button_frame, text="Update data", command=update_data).grid(
    row=0, column=2, padx=5
)
Button(button_frame, text="Delete data", command=delete_data).grid(
    row=0, column=3, padx=5
)


# 276. Creating A TreeView
tree_frame = Frame(root)
tree_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(
    tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse"
)  # poveži scrollbar i treeview, selectmode="browse" znači da korisnik može birati samo jednu stavku
tree.pack()
# kada scrollamo želimo da se i treeview scrolla
tree_scroll.config(command=tree.yview)

# definirajmo stupce
tree["columns"] = ("students_id", "name", "address", "age", "number")
# kofiguriraj stupce
tree.column("#0", width=0, stretch=NO)
tree.column("students_id", anchor=CENTER, width=80)
tree.column("name", anchor=CENTER, width=120)
tree.column("address", anchor=CENTER, width=80)
tree.column("age", anchor=CENTER, width=50)
tree.column("number", anchor=CENTER, width=120)
# definiraj header i text
tree.heading("#0", text="", anchor=CENTER)
tree.heading("students_id", text="ID", anchor=CENTER)
tree.heading("name", text="Name", anchor=CENTER)
tree.heading("address", text="Address", anchor=CENTER)
tree.heading("age", text="Age", anchor=CENTER)
tree.heading("number", text="Phone number", anchor=CENTER)


refresh_treeview()

root.mainloop()
