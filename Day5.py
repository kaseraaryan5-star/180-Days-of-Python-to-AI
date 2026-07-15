#CH - 4 (Dictionary and Sets)

#Dictionary
info = {
    "name" : "Aryan Kasera",
    "age" : 18,
    "learning" : "coding",
    "marks" : 79.8
}
print(info)
print(info["name"])
print(info["marks"])

# Nested Dictionary
student = {
    "name" : "Yashasvi Kasera",
    "subjects" : {
        "phy" : "97",
        "chem" : "98",
        "math" : "99"
    }
}
print(student)

# Methods of Dictionary
student = {
    "name" : "Yashasvi Kasera",
    "subjects" : {
        "phy" : "97",
        "chem" : "98",
        "math" : "99"
    }
}
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))
new_student = {"name" : "Aryan Kasera","city" : "Sailana"}
student.update(new_student)
print(student)

#Sets
collection = {1,2,3,4,"ARYAN","KASERA"}
print(collection)
print(type(collection))

collection = set()   #empty set
print(type(collection))

# Methods of Sets
collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
print(collection)
coll = {1,2,3,4,5}
coll.remove(3)
print(coll)
collect = {"python","ARYAN","YASHASVI",3,5,7,8}
print(collect.clear())
print(len(collect))
colle = {"python","ARYAN","YASHASVI",3,5,7,8}
print(colle.pop())
set1 = {1,2,3,4}
set2 = {2,3,4,5}
print(set.union(set2))
print(set.intersection(set2))

# Practice Question
dictionary = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture","lists of facts and figures"]
}
print(dictionary)

subjects = {"python", "java", "c++", "python", "javascript", "java",
            "python", "java", "c++" , "c"
}
print(subjects)
print(len(subjects))

marks = {}
x = int(input("enter phy :"))
marks.update({"phy" : x})
x = int(input("enter chem :"))
marks.update({"chem" : x})
x = int(input("enter math :"))
marks.update({"math" : x})
print(marks)

values = {
    ("float",9.0),
    ("int",9)
}
print(values)