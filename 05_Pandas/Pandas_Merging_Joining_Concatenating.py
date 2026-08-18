import numpy as np
import pandas as pd
import matplotlib.pyplot as plt   

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

#Questions
# 1.find total revenue generated
total = regs.merge(courses,how="inner",on='course_id')['price'].sum()
print(total)

# 2.find month by month revenue
temp_df = pd.concat([nov,dec],keys=['Nov','Dec']).reset_index()
print(temp_df.merge(courses, how='inner', on='course_id').groupby('level_0')['price'].sum())

# 3.print the registration table
# cols -> name -> course -> price
print(regs.merge(students,on='student_id').merge(courses,on='course_id')[['name','course_name','price']])

# 4.plot the bar chart for revenue/course
print(regs.merge(courses,on='course_id').groupby('course_name')['price'].sum().plot(kind='bar'))
#print(plt.show())

# 5.find students who enrolled in both the month
common_students_id = np.intersect1d(nov['student_id'],dec['student_id'])
print(common_students_id)
print(students[students['student_id'].isin(common_students_id)])

# 6.find course that got no enrollment
course_id_list = np.setdiff1d(courses['course_id'],regs['course_id'])
print(courses[courses['course_id'].isin(course_id_list)])

# 7.find students who did not enroll into any courses
student_id_list = np.setdiff1d(students['student_id'],regs['student_id'])
print(students[students['student_id'].isin(student_id_list)].shape[0])

# 8.print students name -> partner name for all enrolled students
# self join
print(students.merge(students,how='inner',left_on='partner',right_on='student_id')[['name_x','name_y']])

# 9.find top 3 students who did most number enrollments
print(regs.merge(students,how='inner', on='student_id').groupby(['student_id','name'])['name'].count().sort_values(ascending=False).head(3))

# 10.find top 3 students who spent most amount of money on courses
print(regs.merge(students,on='student_id').merge(courses,on='course_id').groupby(['student_id','name'])['price'].sum().sort_values(ascending=False).head(3))

# Alternate syntax for merge
print(pd.merge(students,regs,how= 'inner',on='student_id'))

#IPL Problems
# 1.find top 3 stadiums with highest sixes/matches ratio
temp_df = delivery.merge(matches,left_on='match_id',right_on='id')
six_df = temp_df[temp_df['batsman_runs'] == 6]
num_sixes = six_df.groupby('venue')['venue'].count()
num_matches = matches['venue'].value_counts()
print((num_sixes/num_matches).sort_values(ascending=False).head(3))

# 2.find orange cap holder of all season
print(temp_df.groupby(['season','batsman'])['batsman_runs'].sum().reset_index().sort_values('batsman_runs',ascending=False).drop_duplicates(subset=['season'],keep='first').sort_values('season'))

