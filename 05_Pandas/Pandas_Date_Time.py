import numpy as np 
import pandas as pd

# Timestamp Object
#time stamps reference particular moments in time.(e.g., Oct 12th, 2007 at 7:00pm)

#Creating timestamp object
#creating a timestamp
print(pd.Timestamp('2026/8/20'))

#variations
print(pd.Timestamp('2026-8-20'))
print(pd.Timestamp('2026, 8, 20'))

#only year
print(pd.Timestamp('2026'))

#using text
print(pd.Timestamp('20th August, 2026'))

#providing time also
print(pd.Timestamp('20th August, 2026 9:36AM'))


#using datetime.datetime object
import datetime as dt

x = pd.Timestamp(dt.datetime(2026,8,20,9,40))
print(x)

#fetching attributes
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)

# why seperate objects to handle data and time when python already has datetime funtionality?
# syntax wise datetime is very convenient
# but the perfromance takes a hit while working with huge data. List vs NumPy Array
# the weaknesses of Python's datetime format inspired the NumPy team to add a set of native time series data type to NumPy
# the datetime64 dtype encodes dates as 64-bites integers, and thus allows arrays of dates to be represented very compactly

import numpy as np
date = np.array(['2026-08-20'], dtype='datetime64[D]')
print(date)

print(date + np.arange(12))

# because of the uniform type in NumPy datetime64 arrays, this type of operation can be accomplished much more quickly than if we were working directly with Pyhton's datetime objects, especially as arrays get large
# Pandas Timestamp objects combines the ease-of-use of Python datetime with the efficient storage and vectorized interface of NumPy,datetime64
# from a group of these Timestamp objects, Pandas can construct a DatetimeIndex that can be used to index data in a Series or DataFrame



# DatetimeIndex Object
# a collection of pandas timestamp
#from strings
print(pd.DatetimeIndex(['2023/1/1','2024/1/1','2025/1/1','2026/1/1']))

#using python datetime object
print(pd.DatetimeIndex([dt.datetime(2023,1,1),dt.datetime(2024,1,1),dt.datetime(2025,1,1),dt.datetime(2026,1,1)]))

#using pd.Timestamp
dt_index = pd.DatetimeIndex([pd.Timestamp(2023,1,1),pd.Timestamp(2024,1,1),pd.Timestamp(2025,1,1),pd.Timestamp(2026,1,1)])
print(dt_index)

#using DatetimeIndex as series index
print(pd.Series([1,2,3,4],index=dt_index))



#date_range function
#generate daily dates in a given range
print(pd.date_range(start='2026/8/1' ,end='2026/10/12' ,freq='D'))
print(pd.date_range(start='2026/8/1' ,end='2026/10/12' ,freq='2D'))
print(pd.date_range(start='2026/8/1' ,end='2026/10/12' ,freq='3D'))

#alternate days in a given range
print(pd.date_range(start='2026/8/1' ,end='2026/10/12' ,freq= '3D'))

#B -> business days
print(pd.date_range(start='2026/8/1' ,end='2026/10/12' ,freq= 'B'))

#W -> one week per day
print(pd.date_range(start='2026/8/1' ,end='2026/10/12' ,freq= 'W'))

#h -> hourly data(factor)
print(pd.date_range(start='2026/8/1' ,end='2026/10/12' ,freq= 'h'))

#ME -> month ending
print(pd.date_range(start='2026/8/1' ,end='2026/10/12' ,freq= 'ME'))

#MS -> month starting
print(pd.date_range(start='2026/8/1' ,end='2026/10/12' ,freq= 'MS'))

#A -> year end
print(pd.date_range(start='2026/8/1' ,end='2033/10/12' ,freq= '3D'))

#using periods(number of results)
print(pd.date_range(start='2026/8/1' ,periods=30 ,freq= 'h'))



#to_datetime function
#converts an existing object to pandas timestamp/datetimeindex object
#simple series example
s = pd.Series(['2026/1/1','2025/1/1','2024/1/1'])
print(pd.to_datetime(s).dt.year)
print(pd.to_datetime(s).dt.month)
print(pd.to_datetime(s).dt.day)
print(pd.to_datetime(s).dt.month_name)
print(pd.to_datetime(s).dt.day_name)

#with errors
s = pd.Series(['2026/1/1','2025/1/1','2024/70/1'])
print(pd.to_datetime(s,errors='coerce').dt.year)
print(pd.to_datetime(s,errors='coerce').dt.month)
print(pd.to_datetime(s,errors='coerce').dt.day)
print(pd.to_datetime(s,errors='coerce').dt.month_name)
print(pd.to_datetime(s,errors='coerce').dt.day_name)


df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/expense_data.csv')
print(df.shape)
print(df.head())

df['Date'] = pd.to_datetime(df['Date'])
print(df.info())


#dt accessor
#accessor object for datetimelike properties of the Series values
print(df['Date'].dt.year)
print(df['Date'].dt.month)
print(df['Date'].dt.day)
print(df['Date'].dt.month_name)
print(df['Date'].dt.day_name)
print(df['Date'].dt.is_month_end)
print(df['Date'].dt.is_quarter_end)

#plot graph
import matplotlib.pyplot as plt
print(plt.plot(df['Date'],df['INR']))
print(plt.show())

#day name wise bar chart
df['day_name'] = df['Date'].dt.day_name()
print(df.head())
print(df.groupby('day_name')['INR'].sum().plot(kind='bar'))
print(plt.show())

#month wise bar chart 
df['month_name'] = df['Date'].dt.month_name()
print(df.head())
print(df.groupby('month_name')['INR'].sum().plot(kind='bar'))
print(plt.show())