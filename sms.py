import time
from tkinter import *
from tkinter import ttk, Entry, messagebox
import pymysql
import ttkthemes


def search_student():
    def search_data():
        query = 'select * from student where id=%s OR name=%s OR email=%s OR mobile=%s OR address=%s OR gender=%s OR dob=%s'
        mycursor.execute(query, (
            idEntry.get(), nameEntry.get(), emailEntry.get(), phoneEntry.get(), addressEntry.get(),
            genderEntry.get(), dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('', END, values=data)  # atomatski pretvara u listu

    search_window = Toplevel()
    search_window.grab_set()  # ako kliknem izvan prozora neće pasti iza
    search_window.resizable(False, False)
    search_window.geometry('480x550+730+230')
    search_window.title('Search Student')
    search_window.resizable(False, False)

    idLabel = Label(search_window, text='Id', font=('arial', 20))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky="w")
    idEntry = Entry(search_window, font=('Helvetica', 15, 'bold'), bd=2)
    idEntry.grid(row=0, column=1, pady=15)

    nameLabel = Label(search_window, text='Name', font=('arial', 20))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky="w")
    nameEntry = Entry(search_window, font=('Helvetica', 15, 'bold'), bd=2)
    nameEntry.grid(row=1, column=1, pady=15)

    emailLabel = Label(search_window, text='Email', font=('arial', 20))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky="w")
    emailEntry = Entry(search_window, font=('Helvetica', 15, 'bold'), bd=2)
    emailEntry.grid(row=3, column=1, pady=15)

    phoneLabel = Label(search_window, text='Phone', font=('arial', 20))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky="w")
    phoneEntry = Entry(search_window, font=('Helvetica', 15, 'bold'), bd=2)
    phoneEntry.grid(row=2, column=1, pady=15)

    addressLabel = Label(search_window, text='Address', font=('arial', 20))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky="w")
    addressEntry = Entry(search_window, font=('Helvetica', 15, 'bold'), bd=2)
    addressEntry.grid(row=4, column=1, pady=15)

    genderLabel = Label(search_window, text='Gender', font=('arial', 20))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky="w")
    genderEntry = Entry(search_window, font=('Helvetica', 15, 'bold'), bd=2)
    genderEntry.grid(row=5, column=1, pady=15)

    dobLabel = Label(search_window, text='DOB', font=('arial', 20))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky="w")
    dobEntry = Entry(search_window, font=('Helvetica', 15, 'bold'), bd=2)
    dobEntry.grid(row=6, column=1, pady=15)

    search_student_button = ttk.Button(search_window, text="Search Student", command=search_data)
    search_student_button.grid(row=7, column=1)


def add_student():
    def add_data():
        if (idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get() == '' or emailEntry.get() == ''
                or addressEntry.get() == '' or genderEntry.get() == '' or dobEntry.get() == ''):
            messagebox.showerror('Error', 'All fields are required!!!', parent=add_window)
        else:
            currentdate = time.strftime('%d.%m.%Y')
            currenttime = time.strftime('%H:%M:%S')
            try:
                query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,
                                 (
                                     idEntry.get(), nameEntry.get(), phoneEntry.get(), emailEntry.get(),
                                     addressEntry.get(),
                                     genderEntry.get(), dobEntry.get(), currentdate, currenttime))
                conn.commit()  # execute zapis prem bazi
                result = messagebox.askyesno('Data Entry',
                                             'Data added successfully. Do you want to clean the form')  # oš očistiti
                # formu?
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    phoneEntry.delete(0, END)
                    emailEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    genderEntry.delete(0, END)
                    dobEntry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('Error', 'Id already exist', parent=add_window)
                return

            query = 'select * from student'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                studentTable.insert('', END, values=data)

    add_window = Toplevel()
    add_window.grab_set()  # ako kliknem izvan prozora neće pasti iza
    add_window.resizable(False, False)
    add_window.geometry('480x550+730+230')
    add_window.title('Add student')
    add_window.resizable(False, False)

    idLabel = Label(add_window, text='Id', font=('arial', 20))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky="w")
    idEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), bd=2)
    idEntry.grid(row=0, column=1, pady=15)

    nameLabel = Label(add_window, text='Name', font=('arial', 20))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky="w")
    nameEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), bd=2)
    nameEntry.grid(row=1, column=1, pady=15)

    phoneLabel = Label(add_window, text='Phone', font=('arial', 20))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky="w")
    phoneEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), bd=2)
    phoneEntry.grid(row=2, column=1, pady=15)

    emailLabel = Label(add_window, text='Email', font=('arial', 20))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky="w")
    emailEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), bd=2)
    emailEntry.grid(row=3, column=1, pady=15)

    addressLabel = Label(add_window, text='Address', font=('arial', 20))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky="w")
    addressEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), bd=2)
    addressEntry.grid(row=4, column=1, pady=15)

    genderLabel = Label(add_window, text='Gender', font=('arial', 20))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky="w")
    genderEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), bd=2)
    genderEntry.grid(row=5, column=1, pady=15)

    dobLabel = Label(add_window, text='DOB', font=('arial', 20))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky="w")
    dobEntry = Entry(add_window, font=('Helvetica', 15, 'bold'), bd=2)
    dobEntry.grid(row=6, column=1, pady=15)

    add_student_button = ttk.Button(add_window, text="Add Student", command=add_data)
    add_student_button.grid(row=7, column=1)


def connect_database():
    def connect():
        global mycursor, conn
        try:
            # conn = pymysql.connect(host=hostnameEntry.get(), user=usernameEntry.get(), password=passwordEntry.get())
            conn = pymysql.connect(host='localhost', user='root', password='toor')
            mycursor = conn.cursor()
        except:
            messagebox.showerror('Error', 'Invalid access', parent=connectWindow)
            return
        try:
            query = 'create database studentmanagementsystem'
            mycursor.execute(query)
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
            query = ('create table student(id int not null primary key, name varchar(30), mobile varchar(10), '
                     'email varchar(30), address varchar(100), gender varchar(20), dob varchar(30), date varchar(50), '
                     'time varchar(50))')
            mycursor.execute(query)
        except:
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database connection is successful!', parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)

    connectWindow = Toplevel()
    connectWindow.grab_set()  # ako kliknem izvan prozora neće pasti iza
    connectWindow.geometry('480x250+730+230')
    connectWindow.title('Connect to database')
    connectWindow.resizable(False, False)

    hostnameLabel = Label(connectWindow, text='Host Name', font=('arial', 20))
    hostnameLabel.grid(row=0, column=0, padx=30)
    hostnameEntry = Entry(connectWindow, font=('Helvetica', 15, 'bold'), bd=2)
    hostnameEntry.grid(row=0, column=1, padx=0, pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20))
    usernameLabel.grid(row=1, column=0, padx=30)
    usernameEntry = Entry(connectWindow, font=('Helvetica', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=0, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20))
    passwordLabel.grid(row=2, column=0, padx=30)
    passwordEntry = Entry(connectWindow, font=('Helvetica', 15, 'bold'), bd=2, show='*')
    passwordEntry.grid(row=2, column=1, padx=0, pady=20)

    connect_button = ttk.Button(connectWindow, text='CONNECT', command=connect)
    connect_button.grid(row=3, column=1)


def clock():
    currentdate = time.strftime('%d.%m.%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'Date: {currentdate}\nTime: {currenttime}')
    datetimeLabel.after(1000, clock)


count = 0
text = ''


def slider():
    global text, count  # nemožemo mijenjati varijablu unutar funkcije pa je stavljamo u global(scope)
    if count == len(s):  # kada count stigne do kraja dužine texta resetiraj ih na nulu
        count = 0
        text = ''
    text += s[count]
    sliderlabel.config(text=text)
    count += 1
    sliderlabel.after(300, slider)


root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1280x700')
root.title('Student Management System')
root.resizable(False, False)

datetimeLabel = Label(root, text='', font=('Helvetica', 18, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()

s = 'Student Management System'
sliderlabel = Label(root, text=s, font=('Helvetica', 28, 'bold'), width=30)
sliderlabel.place(x=200, y=0)
slider()

# connect to database
connectButton = ttk.Button(root, text='Connect to database', command=connect_database)
connectButton.place(x=980, y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

logo_image = PhotoImage(file='images/students.png')
logo_Label = Label(leftFrame, image=logo_image)
logo_Label.grid(row=0, column=0)

addstudentButton = ttk.Button(leftFrame, text='Add Student', width=13, state=DISABLED, command=add_student)
addstudentButton.grid(row=1, column=0, pady=10)

searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=13, state=DISABLED, command=search_student)
searchstudentButton.grid(row=2, column=0, pady=10)

deletestudentButton = ttk.Button(leftFrame, text='Delete Student', width=13, state=DISABLED)
deletestudentButton.grid(row=3, column=0, pady=10)

updatestudentButton = ttk.Button(leftFrame, text='Update Student', width=13, state=DISABLED)
updatestudentButton.grid(row=4, column=0, pady=10)

showstudentButton = ttk.Button(leftFrame, text='Show Student', width=13, state=DISABLED)
showstudentButton.grid(row=5, column=0, pady=10)

exportstudentButton = ttk.Button(leftFrame, text='Export Student', width=13, state=DISABLED)
exportstudentButton.grid(row=6, column=0, pady=10)

exitButton = ttk.Button(leftFrame, text='Exit', width=13)
exitButton.grid(row=7, column=0, pady=10)

# sada radimo drugi frame i treeview pogled(ustvari tablica za pregled podataka)
rightFrame = Frame(root, bg='gray')
rightFrame.place(x=350, y=80, width=820, height=600)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame, columns=(
    'Id', 'Name', 'MobileNumber', 'Email', 'Address', 'Gender', 'DOB', 'DateAdded', 'AddedTime'),
                            xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

studentTable.pack(fill=BOTH, expand=1)

studentTable.heading('Id', text='Id')
studentTable.heading('Name', text='Name')
studentTable.heading('MobileNumber', text='Mobile Number')
studentTable.heading('Email', text='Email')
studentTable.heading('Address', text='Address')
studentTable.heading('Gender', text='Gender')
studentTable.heading('DOB', text='D.O.B.')
studentTable.heading('DateAdded', text='Date Added')
studentTable.heading('AddedTime', text='Time Added')

studentTable.config(show="headings")

root.mainloop()
