import numpy as np
import pandas as pd

courses = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/courses.csv')
print(courses)

students = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/students.csv')
print(students)

nov = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/reg-month1.csv')
print(nov)

dec = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/reg-month2.csv')
print(dec)

matches = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/matches(1).csv')
print(matches)

delivery = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/deliveries (1).csv')
print(delivery)

#pd.concat
regs = pd.concat([nov,dec],ignore_index=True)
print(regs)

#Multiindex DataFrame
multi = pd.concat([nov,dec],keys=['Nov','Dec'])
print(multi)
print(multi.loc['Nov'])
print(multi.loc['Dec'])
print(multi.loc['Nov',4])

#add horizontally dataframes
print(pd.concat([nov,dec],axis=1))



#Merge
#inner join
print(students.merge(regs,how='inner',on='student_id'))

#left join
print(courses.merge(regs,how='left',on='course_id'))

temp_df = pd.DataFrame({
    'student_id':[26,27,28],
    'name':['Nitish','Ankit','Rahul'],
    'partner':[28,26,17]
})
students = pd.concat([students,temp_df],ignore_index=True)
print(students.tail())

#right join
print(students.merge(regs,how='right',on='student_id'))

#outer join
print(students.merge(regs,how='outer',on='student_id'))