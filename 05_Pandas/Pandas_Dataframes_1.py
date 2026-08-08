import numpy as np
import pandas as pd

#Creating DataFrame
#using lists
df_student= [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,5],
]
stu= pd.DataFrame(df_student,columns=["IQ","marks","package"])
print(stu)

#using dictionary
student_dict = {
    "IQ":[100,90,120,80],
    "marks":[80,70,100,50],
    "package":[10,7,14,5],
}
students = pd.DataFrame(student_dict)
print(students)

#using read_csv
movies = pd.read_csv("05_Pandas/movies.csv")
print(movies)
ipl = pd.read_csv("05_Pandas/ipl-matches.csv")
print(ipl)



#DataFrame Attributes and Methods
#shape
print(movies.shape)
print(ipl.shape)

#dtypes
print(movies.dtypes)
print(ipl.dtypes)

#index 
print(movies.index)
print(ipl.index)

#columns
print(movies.columns)
print(ipl.columns)

#values
print(movies.values)
print(ipl.values)

#head 
print(movies.head(3))
print(ipl.head(5))

#tail
print(movies.tail(5))
print(ipl.tail(4))

#sample
print(movies.sample(5))
print(ipl.sample(4))

#info
print(movies.info())
print(ipl.info())

#describe
print(movies.describe())
print(ipl.describe())

#isnull
print(movies.isnull().sum())
print(ipl.isnull().sum())

#duplicated
print(movies.duplicated().sum())
print(ipl.duplicated().sum())

# #rename
# print(df_student.rename(columns={"IQ":"intelligence","marks":"score","package":"salary"}, inplace=True))



#Mathematical Operations
#sum
print(students.sum())

#product
print(students.prod())

#mean
print(students.mean())

#median
print(students.median())

#mode 
print(students.mode())

#min 
print(students.min())

#max
print(students.max())

#std
print(students.std())

#var
print(students.var())

