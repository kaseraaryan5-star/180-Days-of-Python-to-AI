# Methods
class Student:
    college_name = "Government College Sailana"

    def __init__(self,marks,name):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks
    
s1 = Student("Vaidehi", 99)
s1.welcome()
print(s1.get_marks())

# Practice Question
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val 
        print("hi", self.name , "your avg score is :", sum/3)

s1 = Student("Damru bhai",[99,93,97])
s1.get_avg()

# Static Method
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is :", sum/3)

s1 = Student("Aryan Kasera", [99,100,100])
s1.get_avg()
s1.hello()


