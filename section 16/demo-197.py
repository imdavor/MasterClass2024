# 193. Creating Menu
# 192. Student Management System Using OOP
# 1. kreiramo klasu Student
class Student:
    def __init__(self, name, age, roll_number):  # atributi
        # inicijalizacija atributa sa kojima ćemo kreirati student objekt
        self.name = name
        self.age = age
        self.roll_number = roll_number


# 2. kreiramo klasu School
class School:
    def __init__(self):
        self.students = []

    # 6. definiramo metodu dodavanja studenta u listu
    def add_student(self, name, age, roll_number):
        student = Student(name, age, roll_number)  # 5. sad kreiramo student objekt iz inputa
        self.students.append(student)  # dodamo studenta na listu

    # def metode koja će prikazati listu
    def display_students(self):
        for student in self.students:
            # print(f'Student name: {student.name}, Age; {student.age}, Roll number: {student.roll_number}')
            print(f'Name: {student.name}, Age: {student.age}, Roll number: {student.roll_number}')
            print('********************')

    def edit_student(self, roll_number, new_name, new_age):
        for student in self.students:
            if student.roll_number == roll_number:
                student.name = new_name
                student.age = new_age
                print(f'*************** Student {student.name} successfully edited!******************')
                return

    def delete_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f'*************** Student {student.name} successfully deleted!******************')
                print('********************')
                return


school = School()  # 3. kreirali smo School objekt

# 7. kreiramo menu
while True:
    choice = input(
        'Enter your choice: \n1. Add student\n2. Display list of students\n3. Edit student data\n4. Delete student data\n5.Quit\n')
    if choice == '1':
        # 4.
        name = input('Enter name: ')
        age = input('Enter age: ')
        roll_number = input('Enter roll number: ')
        school.add_student(name, age, roll_number)  # kreirali smo student objekt i dodali inpute
    elif choice == '2':
        print(f'Students in class:')
        school.display_students()
    elif choice == '3':
        roll_number = input('Enter roll number wich you want to edit: ')
        new_name = input('Enter new name: ')
        new_age = input('Enter new age: ')
        school.edit_student(roll_number, new_name, new_age)
    elif choice == '4':
        roll_number = input('Enter roll number of student wich you want to delete: ')
        school.delete_student(roll_number)
    elif choice == '5':
        break
