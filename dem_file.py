# name=input("Enter your name:")
# f = open("demofile.txt", "w")
# f.write(f"My roll nbr is 128 and my name is {name}")




class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


def fun():
    n = int(input("Enter the number of students: "))

    students = []
    for i in range(n):
        print(f"\nEnter details of student {i + 1}:")
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        student = Student(name, age)
        students.append(student)

    file_name = "student_data.txt"
    with open("student_data.txt", "w") as file:
        for student in students:
            file.write(f"Name: {student.name}, Age: {student.age}\n")
        print(f"\nStudent data has been stored in '{file_name}'.")


fun()
