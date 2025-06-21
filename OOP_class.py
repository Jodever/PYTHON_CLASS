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





John = Student("John", 21, 230221001, "Mechanical", "Engineering", 4.86)
Ife = Student("Ife", 21, 230231009, "CPE", "Engineering", 4.86)

# print(f'Name is {John.name}')
# print(f'Age:{John.age}')
# print(f'Department is:{John.department}')
# print(f'GPA:{John.GPA}')

# print(f'Name is {Ife.name}')
# print(f'Age:{Ife.age}')
# print(f'Department is:{Ife.department}')
# print(f'GPA:{Ife.GPA}')

