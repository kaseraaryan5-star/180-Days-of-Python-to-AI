# "del" Keyword
# Used to delete object properties pr pbject itself

class Student :
   def __init__(self,name):
        self.name  = name

s1 = Student("Aryan")

del s1
print(s1.name)        

# Private(like) attributes & methods

class Person:
    __name = "aryan"

    def __hello():
        print("hello person !")

p1  = Person()
print(p1.__name)

class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person !")
    
    def welcome(self):
       self .__hello()

p1 = Person()
print(p1.welcome())

# Inheritance
# 1. Single Inheritance

class Car:
    colour = "Black"
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())

# 2. Multi-level Inheritance

class Car:
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
                   
car1 = Fortuner("diesel")
car1.start()

# 3. Multiple Inheritance

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)

class Car:
    def __init__(self,car_type):
        self.type = car_type

        @staticmethod
        def start():
            print("Car started....")
        
        @staticmethod
        def stop():
            print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self,name, car_type):
        super().__init__(car_type)
        self.name = name
        Car.start()

car1 = ToyotaCar("prius", "electric")
print(car1.type)

# Class Methods

class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)

# Property decorator
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem 
        self.math = math

        @property
        def percentage(self):
            return str((self.phy + self.chem + self.math)/3) + "%"
        
stu1 = Student(98,97,99)
print(stu1.percentage)

stu1.phy = 88
print(stu1.percentage)

