import pandas as pd

# WORKING WITH JSON FILES
df = pd.read_json('/Users/aryankasera/Desktop/100-Days-AI/07_Machine_learning.py/train.json')
print(df)

df = pd.read_json('https://api.exchangerate-api.com/v4/latest/INR')
print(df)

# WORKING WITH SQL FILES
import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='',database='world')
print(conn)

print(pd.read_sql_query("SELECT * FROM city WHERE CountryCode LIKE 'IND'",conn))

