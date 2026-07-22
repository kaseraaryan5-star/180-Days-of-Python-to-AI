# CH - 8 (Object Oriented Programming)

class Student:
    name = "Aryan"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

class car:
    colour = "White"
    brand = "BMW"

car1 = car()
print(car1.colour)
print(car1.brand)

# __init__ function
class Student:
    name = "Aryan"
    def __init__(self):
        print("adding new studnet in database.... ")

s1 = Student()

class Student:
    name = "Aryan"
    def __init__(self):
        print(self)
        print("adding new students in database.....")

s1 = Student()
print(s1)

class Student:

    # Default constructors
    def __init__(self):
        pass

    # Parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new students in database.....")

s1 = Student("Aryan", 95)
print(s1.name,s1.marks)

s2 = Student("Yashasvi", 99)
print(s2.name,s2.marks)

# Class & Instance Attributes
class Student:
    college = "Government College Sailana"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new students in database..........")

s1 = Student("Aryan", 99)
print(s1.name,s1.marks)

s2 = Student("Yashasvi", 100)
print(s2.name,s2.marks)

print(s2.college)