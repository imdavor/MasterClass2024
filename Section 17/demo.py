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


def delete_data():
    student_id = input("Enter student id you want to delete: ")
    conn = psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432",
    )
    cur = conn.cursor()  # moraš kreirati kursor
    cur.execute("SELECT * FROM students WHERE students_id = %s", (student_id,))
    student = cur.fetchone()  # uhvati red iz tablice
    if student:  # da li postoji student sa tim id-em
        print(
            f"Student with id {student_id} found>>> ID = {student[0]} Name = {student[1]}, Address = {student[2]}, Age = {student[3]}, Number = {student[4]}"
        )
        choice = input("Do you want to delete this student? (y/n): ")
        if choice.lower() == "y":
            cur.execute("DELETE FROM students WHERE students_id = %s", (student_id,))
            print("Data deleted successfully!")
        else:
            print("Data not deleted!")
    else:
        print("Student not found!")
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


def read_data():
    conn = psycopg2.connect(
        dbname="studentdb",
        user="postgres",
        password="admin123",
        host="localhost",
        port="5432",
    )
    cur = conn.cursor()  # moraš kreirati kursor
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()  # uhvati sve redove iz tablice
    for student in students:
        print(
            f"ID = {student[0]} Name = {student[1]}, Address = {student[2]}, Age = {student[3]}, Number = {student[4]}"
        )
    conn.commit()
    conn.close()


# insert_data()
# update_data()
# delete_data()

while True:
    print("Welcome to Student Management Database System")
    print("1. Create table")
    print("2. Insert data")
    print("3. Read data")
    print("4. Delete data")
    print("5. Update data")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        create_table()
    elif choice == "2":
        insert_data()
    elif choice == "3":
        read_data()
    elif choice == "4":
        delete_data()
    elif choice == "5":
        update_data()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
