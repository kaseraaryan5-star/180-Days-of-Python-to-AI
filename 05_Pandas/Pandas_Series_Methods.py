import numpy as np
import pandas as pd

subs = pd.read_csv("/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/subs.csv").squeeze("columns")
print(subs)

vk = pd.read_csv("/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/kohli_ipl.csv",index_col = 0).squeeze("columns")
print(vk)

Bollywood = pd.read_csv("/Users/aryankasera/Desktop/180-Days-Python/05_Pandas/bollywood.csv",index_col = 0).squeeze("columns")
print(Bollywood)

#Some Important Series Methods
#astype
import sys 
print(sys.getsizeof(vk))
print(sys.getsizeof(vk.astype('int16')))

#between
print(vk[vk.between(51,99)].size)

#clip
print(subs.clip(100,200))

#drop_duplicates
temp = pd.Series([1,1,2,2,3,3,4,4])
print(temp)
print(temp.drop_duplicates(keep='last'))

#isnull
temp1 = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])
print(temp1)
print(temp1.isnull().sum())

#dropna
print(temp1.dropna())

#fillna
print(temp1.fillna(temp1.mean()))

#isin
print(vk[vk.isin([49,99,89])])

#apply
print(Bollywood.apply(lambda x:x.split()[0].upper()))

