import numpy as np 
import pandas as pd

#What are vectorized operations
a = np.array([1,2,3,4])
print(a)

#problem in vectorized operation in vanilla python
#s = ['cat','mat',None,'rat']
#[i.startswith('c') for i in s]

#How pandas solve this issue?
s = pd.Series(['cat','mat',None,'rat'])
#string accessor
print(s.str.startswith('c'))

#import titanic
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/titanic.csv')
print(df)
print(df.head())
print(df['Name'])



#Common Functions
#lower/upper/captalize/title
print(df['Name'].str.lower())
print(df['Name'].str.upper())
print(df['Name'].str.capitalize())
print(df['Name'].str.title())

#len
print(df['Name'][df['Name'].str.len() == 82].values[0])

#strip
print(('           Aryan           ').strip())

#split -> get
df['lastname'] = df['Name'].str.split(',').str.get(0)
print(df.head())

df[['title','firstname']] = df['Name'].str.split(',').str.get(1).str.strip().str.split(' ', n=1, expand=True)
print(df.head())

print(df['title'].value_counts())

#replace
df['title'] = df['title'].str.replace('Ms.','Miss.')
df['title'] = df['title'].str.replace('Mlle.','Miss.')
print(df['title'].value_counts())



#Filtering
#startwith/endswith
print(df[df['firstname'].str.endswith('A')])
print(df[df['firstname'].str.startswith('A')])

#isdigit/isalpha
print(df[df['firstname'].str.isdigit()])
print(df[df['firstname'].str.isalpha()])



#Applying regex
#contains
#search john -> both case
print(df[df['firstname'].str.contains('john',case=False)])

#find last name with starts and ends char vowel
print(df[df['lastname'].str.contains('^[aeiouAEIOU].+[aeiouAEIOU]$')])



#slicing
print(df['Name'].str[::2])