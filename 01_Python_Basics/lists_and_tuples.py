str = "my name is Aryan Kasera"
input(len(str))
print(str[4])
print(str[1:4])
input(str.endswith("ra"))
input(str.capitalize())
input(str.replace("Aryan","Yashasvi"))
input(str.find("a"))
input(str.count("a"))

age = 95
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")


#CH - 3 (LISTS AND TUPLES)
Lists in Python
marks = [98.3, 87.6, 89.6, 56.9, 87.0]
print(marks)
print(type(marks))
print(len(marks))
print(marks[4])
print(marks[3])
student = ["Aryan",78,18,"Sailana"]
print(student)
student[0] = "Yashasvi"
print(student)

#slicing in Lists
marks = [78, 89, 76, 90, 45]
print(marks[1:3])
print(marks[:4])
print(marks[1:])

#List Methods
list = [3, 5, 2, 4, 1] 
list.append(6)
print(list)
list.sort()
print(list)
list.sort(reverse = True)
print(list)
list.reverse()
print(list)
list.insert(3,8)
print(list)
list.remove(5)
print(list)
list.pop(4)
print(list)

#Tuple in Python
tup = ()
print(tup)
print(type(tup))
tup = (1,)
print(tup)
print(type(tup))
tup = (1,2,3,4,2,2,2,)
print(tup[2])
print(tup[1:3])
print(tup.index(3))
print(tup.count(2))

#Practice Question
list = ["Stranger Things","From","Wednesday"]
print(list)

list = ["m", "a", "a", "m"]
copy_list = list.copy()
copy_list.reverse()
if(copy_list == list):
    print("palindrome")
else: 
    print("not palindrome")

grade = ("C","D", "A", "A", "B", "B","A")
print(grade.count("A"))

grade = ["C","D", "A", "A", "B", "B","A"]
grade.sort()
print(grade)
