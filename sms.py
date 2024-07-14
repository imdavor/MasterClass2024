import time
from tkinter import *
from tkinter import ttk, Entry, messagebox
import pymysql
import ttkthemes


def connect_database():
    def connect():
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

addstudentButton = ttk.Button(leftFrame, text='Add Student', width=13, state=DISABLED)
addstudentButton.grid(row=1, column=0, pady=10)

searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=13, state=DISABLED)
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
studentTable.heading('AddedTime', text='Added Time')

studentTable.config(show="headings")

root.mainloop()
