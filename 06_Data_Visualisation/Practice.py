import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print(plt.style.use('default'))

# 2D PLOT 
#plotting a simple function
price = [50000,55000,58000,57000,52000,48000]
year = [2026,2027,2028,2029,2030,2031]

print(plt.plot(year,price))
print(plt.show())

#from a pandas dataframe
batsman = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/sharma-kohli.csv')
print(batsman)
plt.plot(batsman['index'],batsman['V Kohli'])
plt.tight_layout()
plt.show()

#plotting multiple plots
print(plt.plot(batsman['index'],batsman['V Kohli']))
print(plt.plot(batsman['index'],batsman['RG Sharma']))
print(plt.tight_layout())
print(plt.show())

#labels plt.title
print(plt.plot(batsman['index'],batsman['V Kohli']))
print(plt.plot(batsman['index'],batsman['RG Sharma']))

print(plt.title('Rohit Vs Kohli Carrer Comparison'))
print(plt.xlabel('Season'))
print(plt.ylabel('Runs Scored'))
print(plt.tight_layout())
print(plt.show())