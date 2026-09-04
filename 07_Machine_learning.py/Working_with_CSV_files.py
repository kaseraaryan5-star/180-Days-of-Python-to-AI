# 1.Importing Pandas
import pandas as pd

# 2.Opening a local csv file
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/aug_train.csv')
print(df)

# 3.Opening a csv file from an URL
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

print(pd.read_csv(data))

# 4.Sep Parameter
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/movie_titles_metadata.tsv',sep='\t',names=['sno','name','release_year','rating','votes','geners'])
print(df)

# 5.Index_col parameter
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/aug_train.csv',index_col='enrollee_id')
print(df)

# 6.Header parameter 
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/test.csv',header=1)
print(df)

# 7.use_col parameter
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/aug_train.csv',usecols=['enrollee_id','gender','education_level'])
print(df)

# 8.Squeeze parameter
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/aug_train.csv',usecols=['enrollee_id']).squeeze()
print(df)

# 9.Skiprows/nrows Parameter
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/aug_train.csv',skiprows=[0,5],nrows=100)
print(df)

# 10.Encoding Parameter
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/zomato (1).csv',encoding='latin-1')
print(df)

# 11.Skip bad lines
df = pd.read_csv(
    '/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/zomato (1).csv',
    encoding='latin-1',
    on_bad_lines='skip',
    engine='python'
    )
print(df)

# 12.dtypes parameters
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/aug_train.csv',dtype={'target':int})
print(df)

# 13.Handling Dates
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/IPL Matches 2008-2020.csv',parse_dates=['date']).info()
print(df)

# 14.Convertors
def rename(name):
    if name == 'Royal Challengers Banglore':
        return 'RCB'
    else:
        return name

rename('Royal Challengers Banglore')

df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/IPL Matches 2008-2020.csv', converters={'team1':rename})
print(df)

# 15.na_values parameter
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/aug_train.csv',na_values=['Male'])
print(df)

# 16.Loading a huge dataset in chunks
dfs = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/aug_train.csv',chunksize=5000)
print(dfs)

for chunks in dfs:
    print(chunks.shape)
