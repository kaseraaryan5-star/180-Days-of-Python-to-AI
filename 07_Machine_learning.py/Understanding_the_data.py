import pandas as pd

df = pd.read_csv('/Users/aryankasera/Desktop/100-Days-AI/07_Machine_learning.py/train.csv')
print(df)

# 1.How big is the data?
print(df.shape) 

# 2.How does the data look like?
print(df.head())
print(df.sample(5))

# 3.What is the data type of columns?
print(df.info())

# 4.Are there any missing values?
print(df.isnull().sum())

# 5.How does the data look mathematically?
print(df.describe())

# 6.Are there duplicate values?
print(df.duplicated().sum())

# 7.How is the corelation between columns?
print(df.corr(numeric_only=True)['Survived'])
