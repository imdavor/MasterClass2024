import psycopg2


def create_table():
    conn = psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432",
    )
    cur = conn.cursor()  # moraš kreirati kursor
    cur.execute(
        "CREATE TABLE students(students_id SERIAL PRIMARY KEY, name TEXT, address TEXT, age INT, number TEXT);"
    )
    print("Table created successfully")
    conn.commit()
    conn.close()


def insert_data():
    # PRIHVATI USER INPUT
    name = input("Enter name: ")
    address = input("Enter address: ")
    age = input("Enter age: ")
    number = input("Enter number: ")

    conn = psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432",
    )
    cur = conn.cursor()  # moraš kreirati kursor
    cur.execute(
        # "INSERT INTO students(name, address, age, number) VALUES ('Rob', 'CA', 35, '7777777');"
        "INSERT INTO students(name, address, age, number) VALUES (%s,%s,%s,%s)",
        (name, address, age, number),
    )
    print("Data inserted successfully!")
    conn.commit()
    conn.close()


def update_data():
    student_id = input("Enter student id: ")
    conn = psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="admin123",
        host="localhost",
    )
    cur = conn.cursor()  # moraš kreirati kursor
    # dodajmo dictionary fields listu opcija za update pojedinačnog podatka iz tablice
    fields = {
        "1": ("name", "Enter new name: "),  # ovo je tupple (key, value) vrijednost
        "2": ("address", "Enter new address: "),
        "3": ("age", "Enter new age: "),
        "4": ("number", "Enter new number: "),
    }
    print("Select field to update: ")
    for key in fields:
        print(f"{key}: {fields[key][0]}")
    field_choice = input("Enter field number you want to update: ")
    if field_choice in fields:
        field_name, prompt = fields[field_choice]
        new_value = input(prompt)
        sql = f"UPDATE students SET {field_name}=%s WHERE students_id = %s"
        cur.execute(sql, (new_value, student_id))
        print(f"{field_name} updated successfully!")
    else:
        print("Invalid choice. Please try again.")
        return

    conn.commit()
    conn.close()
    print("Data updated successfully!")


# insert_data()
update_data()
