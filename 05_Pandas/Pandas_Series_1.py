import numpy as np
import pandas as pd

#Series in lists 
#string
country = ["India","US","Italy","Netherland"]
pd.Series(country)
print(pd.Series(country))

#integer
runs = [36,47,56,45,88,90]
pd.Series(runs)
print(pd.Series(runs))

#custom index
marks = [67,89,70,80]
subject = ["english","maths","hindi","science"]
pd.Series(marks,index= subject)
print(pd.Series(marks,index=subject))

#setting a name
marks = pd.Series(marks,index=subject,name= "Aryan ke marks")
print(marks)



#Series from dictionary
marks = {
    "maths":89,
    "hindi":79,
    "english":67,
    "science":79
}
marks_series = pd.Series(marks,name= "Aryan ke marks")
print(marks_series)



#Series Attributes
#size
a = marks_series.size
print(a)

#dtype
b = marks_series.dtype
print(b)

#name
c = marks_series.name
print(c)

#is_unique
d = marks_series.is_unique
print(d)

#index
e = marks_series.index
print(e)

#values
f = marks_series.values
print(f)



#Series using read_csv
#with one col
subs = pd.read_csv("/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/subs.csv").squeeze("columns")
print(subs)

#with 2 col
vk = pd.read_csv("/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/kohli_ipl.csv",index_col = 0).squeeze("columns")
print(vk)

Bollywood = pd.read_csv("/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/bollywood.csv",index_col = 0).squeeze("columns")
print(Bollywood)



#Series Methods
#head and tail
#head
a = subs.head()
print(a)
#tail
b = subs.tail(8)
print(b)

#sample
c = Bollywood.sample(7)
print(c)

#value_counts
d = Bollywood.value_counts()
print(d)

#sort_values
e = vk.sort_values()
print(e)

#sort_index
f = Bollywood.sort_index()
print(f)



#Series Maths Methods
#count
a = vk.count()
print(a)

#sum and product
#sum
b = subs.sum()
print(b)
#product
c = subs.product()
print(c)

#mean/median/mode/std/var
#mean
d = subs.mean()
print(d)
#median
e = subs.median()
print(e)
#mode
f = subs.mode()
print(f)
#std
g = subs.std()
print(g)
#var
h = subs.var()
print(h)

#min/max
#min
i = subs.min()
print(i)
#max
j = subs.max()
print(j)

#describe
k = vk.describe()
print(k)



#Series Indexing
#integer indexing
x = pd.Series([24,35,46,89,90,67,99])
print(x[6])

#slicing   (same as python)(Use iloc)
y = pd.Series(Bollywood)
print(y.iloc[::3])

#negative slicing
z = pd.Series(vk)
print(vk.iloc[-8])

#fancy indexing
i = Bollywood.iloc[[4,7,5,8,9]]
print(i)

#indexing with labels    (Use loc)
j = Bollywood.loc["Evening Shadows"]
print(j)



#Editing Series
#using indexing
a = marks_series["english"] = 100
print(marks_series)

#what if an index does not exist.   (it add on the series)
b = marks_series["sst"]= 90
print(marks_series)

#slicing
c = marks_series[2:4]=100
print(marks_series)

#fancy slicing
d = vk[[3,4,5]]=[0,0,0]
print(vk)

#using index label
e = Bollywood["2 States (2014 film)"]= "Alia Bhatt"
print(Bollywood)


#Series with Python Functionalities
#len/type/dir/sorted/max/min
print(len(subs))
print(type(subs))
print(dir(subs))
print(sorted(subs))
print(max(subs))
print(min(subs))

#type conversion
print(list(marks_series))
print(dict(marks_series))

#membership operator
print("Uri: The Surgical Strike" in Bollywood)

#looping
for i in Bollywood.index:
    print(i)

#arithmetic operation(broadcasting)
print(100 - marks_series)

#relational operator
print(vk >= 50)



#Boolean Indexing on Series
#find no. of 50's and 100's scored by kohli
print(vk[vk >= 50].size)

#find no. of ducks
print(vk[vk == 0].size)

#count no. of days when i had more than 200 subs a day
print(subs[subs > 200].size)

#find actor who have done more than 20 movies
num_Bollywood = Bollywood.value_counts()
print(num_Bollywood[num_Bollywood > 20].size)



#Plotting graph on Series
print(subs.plot())
print(Bollywood.value_counts().head(20).plot(kind='pie'))


