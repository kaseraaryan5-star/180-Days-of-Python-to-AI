import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")

# Total_bill ko float mein convert karo (string nahi)
df['total_bill'] = df['total_bill'].astype(float)

print(df.groupby('sex')['total_bill'].mean())
print(df.groupby(["sex", "smoker"])['total_bill'].mean().unstack())
print(df.pivot_table(index='sex', columns='smoker', values='total_bill'))

#aggfunc
print(df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='sum'))

#all columns together
print(df.pivot_table(index='sex',columns='smoker', numeric_only=True))

#multidimensional
print(df.pivot_table(index=['sex','smoker'],columns=['day','time'],values='total_bill'))

#margins
print(df.pivot_table(index='sex',columns='smoker',values='total_bill',aggfunc='sum',margins=True))

#plotting graph
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/expense_data.csv')
print(df)
print(df.head())
print(df['Category'].value_counts())
print(df.info())
df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'])
print(df.info())
df['month'] = df['Date'].dt.month_name()
print(df.head())
print(df.pivot_table(index='month',columns='Category',values='INR',aggfunc='sum',fill_value=0).plot())
plt.show()
print(df.pivot_table(index='month',columns='Income/Expense',values='INR',aggfunc='sum',fill_value=0).plot())
plt.show()
print(df.pivot_table(index='month',columns='Account',values='INR',aggfunc='sum',fill_value=0).plot())
plt.show()
