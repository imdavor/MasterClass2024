import time
from tkinter import *
from tkinter import ttk, Entry, messagebox
import pymysql
import ttkthemes


def toplevel_data(title, button_text, command):
    global idEntry, nameEntry, phoneEntry, emailEntry, addressEntry, genderEntry, dobEntry, screen
    screen = Toplevel()
    screen.grab_set()  # ako kliknem izvan prozora neće pasti iza
    screen.resizable(False, False)
    screen.geometry('480x550+730+230')
    screen.title(title)
    screen.resizable(False, False)

    idLabel = Label(screen, text='Id', font=('arial', 20))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky="w")
    idEntry = Entry(screen, font=('Helvetica', 15, 'bold'), bd=2)
    idEntry.grid(row=0, column=1, pady=15)

    nameLabel = Label(screen, text='Name', font=('arial', 20))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky="w")
    nameEntry = Entry(screen, font=('Helvetica', 15, 'bold'), bd=2)
    nameEntry.grid(row=1, column=1, pady=15)

    emailLabel = Label(screen, text='Email', font=('arial', 20))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky="w")
    emailEntry = Entry(screen, font=('Helvetica', 15, 'bold'), bd=2)
    emailEntry.grid(row=3, column=1, pady=15)

    phoneLabel = Label(screen, text='Phone', font=('arial', 20))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky="w")
    phoneEntry = Entry(screen, font=('Helvetica', 15, 'bold'), bd=2)
    phoneEntry.grid(row=2, column=1, pady=15)

    addressLabel = Label(screen, text='Address', font=('arial', 20))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky="w")
    addressEntry = Entry(screen, font=('Helvetica', 15, 'bold'), bd=2)
    addressEntry.grid(row=4, column=1, pady=15)

    genderLabel = Label(screen, text='Gender', font=('arial', 20))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky="w")
    genderEntry = Entry(screen, font=('Helvetica', 15, 'bold'), bd=2)
    genderEntry.grid(row=5, column=1, pady=15)

    dobLabel = Label(screen, text='DOB', font=('arial', 20))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky="w")
    dobEntry = Entry(screen, font=('Helvetica', 15, 'bold'), bd=2)
    dobEntry.grid(row=6, column=1, pady=15)

    student_button = ttk.Button(screen, text=button_text, command=command)
    student_button.grid(row=7, column=1)

    if title == 'Edit Student':
        indexing = studentTable.focus()
        content = studentTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        phoneEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        genderEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])


def update_data():
    query = (
        'update student set name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s where '
        'id=%s')
    mycursor.execute(query, (nameEntry.get(), phoneEntry.get(), emailEntry.get(), addressEntry.get(),
                             genderEntry.get(), dobEntry.get(), currentdate, currenttime, idEntry.get()))
    conn.commit()
    messagebox.showinfo('Success', f'Id {idEntry.get()} updated successfully!', parent=screen)
    show_student()
    screen.destroy()


def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)


def delete_student():
    # get index of row
    indexing = studentTable.focus()
    print(indexing)
    content = studentTable.item(indexing)
    content_id = content['values'][0]  # vrijednost iz indexiranog podatka u ovom slučaju id
    # a sad stvarno brišemo record
    query = 'delete from student where id=%s'
    mycursor.execute(query, content_id)
    conn.commit()
    messagebox.showinfo('Deleted', f'This {content_id} is Record deleted successfully!')
    # refresh tree view
    # query = 'select * from student'
    # mycursor.execute(query)
    # fetched_data = mycursor.fetchall()
    # studentTable.delete(*studentTable.get_children())
    # for data in fetched_data:
    #     studentTable.insert('', END, values=data)
    show_student()


def search_data():
    query = ('select * from student where id=%s OR name=%s OR email=%s OR mobile=%s OR address=%s OR gender=%s OR '
             'dob=%s')
    mycursor.execute(query, (
        idEntry.get(), nameEntry.get(), emailEntry.get(), phoneEntry.get(), addressEntry.get(),
        genderEntry.get(), dobEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('', END, values=data)  # atomatski pretvara u listu


def add_data():
    if (idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get() == '' or emailEntry.get() == ''
            or addressEntry.get() == '' or genderEntry.get() == '' or dobEntry.get() == ''):
        messagebox.showerror('Error', 'All fields are required!!!', parent=screen)
    else:
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
            messagebox.showerror('Error', 'Id already exist', parent=screen)
            return

        query = 'select * from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('', END, values=data)


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
        show_student()

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
    global currentdate, currenttime
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

addstudentButton = ttk.Button(leftFrame, text='Add Student', width=13, state=DISABLED,
                              command=lambda: toplevel_data('Add Student', 'Add Student', add_data))
addstudentButton.grid(row=1, column=0, pady=10)

searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=13, state=DISABLED,
                                 command=lambda: toplevel_data('Search Student', 'Search Student', search_data))
searchstudentButton.grid(row=2, column=0, pady=10)

deletestudentButton = ttk.Button(leftFrame, text='Delete Student', width=13, state=DISABLED, command=delete_student)
deletestudentButton.grid(row=3, column=0, pady=10)

updatestudentButton = ttk.Button(leftFrame, text='Edit Student', width=13, state=DISABLED,
                                 command=lambda: toplevel_data('Edit Student', 'Update Student', update_data))
updatestudentButton.grid(row=4, column=0, pady=10)

showstudentButton = ttk.Button(leftFrame, text='Show Student', width=13, state=DISABLED, command=show_student)
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

# podesimo širinu columni
studentTable.column('Id', width=50, anchor=CENTER)
studentTable.column('Name', width=100, anchor=CENTER)
studentTable.column('MobileNumber', width=150, anchor=CENTER)
studentTable.column('Email', width=200, anchor=CENTER)
studentTable.column('Address', width=100, anchor=CENTER)
studentTable.column('Gender', width=100, anchor=CENTER)
studentTable.column('DOB', width=100, anchor=CENTER)
studentTable.column('DateAdded', width=100, anchor=CENTER)
studentTable.column('AddedTime', width=100, anchor=CENTER)

# za promjenu bg od treeviewa
style = ttk.Style()
style.configure('Treeview', rowheight=30, font=('helvetica', 11, 'bold'), background='light gray',
                fieldbackground='grey')
# style.configure('Treeview.Heading', font=('helvetica', 12, 'bold'))
studentTable.config(show="headings")
root.mainloop()
