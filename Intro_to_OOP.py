#Classes and objects
#__init__, instance variables
#Create a Student or Car class

"""
What are Classes?
Classes are sort of a frame or template that describes a particular object's features, characteristics and behaviours.

the __int__ keyword aka constructor initialises the predefined characteristics of a particular class,e.g name, etc.

instance variables refers to objects which are real instances of a particular class
"""
#Student class
"""
A student has;
Name
Age
Matriculation No
Department
Faculty
GPA

"""
class Student:
    def __init__(self, name:str, age:int, matriculation_no:int, department:str, Faculty:str, GPA:float):
        self.name = name 
        self.age = age 
        self.matriculation_no = matriculation_no
        self.department = department
        self.Faculty = Faculty
        self.GPA = GPA

    def speak(self):
        return self.name, self.matriculation_no,self.department, self.Faculty,self.age
    # print(f'My details are as follows:{name}, {age},{matriculation_no}, {department}, {Faculty}, {GPA}')




John = Student("John", 21, 230221001, "Mechanical", "Engineering", 4.86)
# a = print(Student.speak("John", 21, 230221009, "Mechanical", "Engineering", 4.00))

# print(Student.speak(John))

student1 = Student("Ife", 20, 240231009, "CPE", "Engineering", 3.88)
# print(Student.speak(Ife))

# print(f'Name is {John.name}')
# print(f'Age:{John.age}')
# print(f'Department is:{John.department}')
# print(f'GPA:{John.GPA}')

# print(f'Name is {Ife.name}')
# print(f'Age:{Ife.age}')
# print(f'Department is:{Ife.department}')
# print(f'GPA:{Ife.GPA}')

# class Student:
#     def __init__(self, name:str, age:int, Matriculation_no:int, Department:str, Faculty:str):
#         self.name = name
#         self.age = age
#         self.Matriculation_no = Matriculation_no
#         self.Department = Department
#         self.Faculty = Faculty

#     def show(self):
#         return self.name, self.age, self.Matriculation_no, self.Department, self.Faculty 



# Okon = Student("Okon", 20, 200211001, "Mechanical engineering", "Engineering")
# # Student.show(Okon)


class Car:
    def __init__(self, brand:str, model:str, color:str):
        self.brand = brand
        self.model = model
        self.color = color


    def show(self) -> None:
        return self.brand, self.model, self.color
    
    def driving(self):
        print("Driving the car", self.brand)
        return None


car1 = Car("Audi", "A4", "Blue")
James_car = Car("Toyota", "spyder", "Red")

# print(Car.driving(car1))
# print(Car.driving(James_car))

# print(Car.show(self=car1))
# print(Car.show(self=James_car))
# with open("Student's Details", mode = 'w', encoding= 'utf-8') as S1:
#     S1.write(str(Student.show(Okon)))

#Methods in classes, self
#Inheritance basics
#datetime

#student and car1

# class Mix(Student, Car):
#     def derived():
#         print("In the derived class")
#         return None


# S1 = Mix.speak(student1)
# D1 = Mix.show(James_car)
# D2 = Mix.driving(James_car)

# print(S1)
# print(D1)
# print(D2)
# Mix.derived()

from datetime import datetime, date, time, timezone
#date = datetime.date(2025, 5, 3)
# time = datetime.datetime.time()
current = datetime.now()


curr = current.strftime('%a %b %y, %H:%M:%S')

#print(date)
# print(time)
print(curr)