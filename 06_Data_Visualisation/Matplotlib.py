import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print(plt.style.use('default'))

# 2D PLOT 
#plotting a simple function
# price = [50000,55000,58000,57000,52000,48000]
# year = [2026,2027,2028,2029,2030,2031]

# print(plt.plot(year,price))
# #print(plt.show())

#from a pandas dataframe
batsman = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/sharma-kohli.csv')
# # print(batsman)
# plt.plot(batsman['index'],batsman['V Kohli'])
# # plt.tight_layout()
# # plt.show()

# #plotting multiple plots
# print(plt.plot(batsman['index'],batsman['V Kohli']))
# print(plt.plot(batsman['index'],batsman['RG Sharma']))
# print(plt.tight_layout())
# print(plt.show())

# #labels plt.title
# print(plt.plot(batsman['index'],batsman['V Kohli']))
# print(plt.plot(batsman['index'],batsman['RG Sharma']))

# print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# print(plt.xlabel('Season'))
# print(plt.ylabel('Runs Scored'))
# print(plt.tight_layout())
# print(plt.show())

# colors(hex) 
# print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue'))
# print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black'))

# print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# print(plt.xlabel('Season'))
# print(plt.ylabel('Runs Scored'))
# print(plt.tight_layout())
# print(plt.show())

# #line(width and style)
# print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashed'))
# print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashed'))

# print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# print(plt.xlabel('Season'))
# print(plt.ylabel('Runs Scored'))
# print(plt.tight_layout())
# print(plt.show())

# print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dotted'))
# print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dotted'))

# print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# print(plt.xlabel('Season'))
# print(plt.ylabel('Runs Scored'))
# print(plt.tight_layout())
# print(plt.show())

# print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashdot'))
# print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashdot'))

# print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# print(plt.xlabel('Season'))
# print(plt.ylabel('Runs Scored'))
# print(plt.tight_layout())
# print(plt.show())

# print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashed',linewidth=6))
# print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashed',linewidth=4))

# print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# print(plt.xlabel('Season'))
# print(plt.ylabel('Runs Scored'))
# print(plt.tight_layout())
# print(plt.show())


# print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashed',linewidth=2,marker='D'))
# print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashed',linewidth=2,marker='o'))

# print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# print(plt.xlabel('Season'))
# print(plt.ylabel('Runs Scored'))
# print(plt.tight_layout())
# print(plt.show())

#legend -> location 
# print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashed',linewidth=2,marker='D',label='Virat'))
# print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashed',linewidth=2,marker='o',label='Rohit'))

# print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# print(plt.xlabel('Season'))
# print(plt.ylabel('Runs Scored'))
# print(plt.legend())
# print(plt.tight_layout())
# print(plt.show())

# #limiting axis
# price = [50000,55000,58000,57000,52000,480000]
# year = [2026,2027,2028,2029,2030,2031]

# print(plt.plot(year,price))
# print(plt.ylim(0,100000))
# print(plt.xlim(2028,2030))
# print(plt.show())

#grid
# print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashed',linewidth=2,marker='D',label='Virat'))
# print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashed',linewidth=2,marker='o',label='Rohit'))

# print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# print(plt.xlabel('Season'))
# print(plt.ylabel('Runs Scored'))
# print(plt.legend())
# print(plt.tight_layout())
# print(plt.show())
# print(plt.grid())





#SCATTER PLOT
#plt.scatter simple function
# x = np.linspace(-10,10,50)

# y = 10*x +3 + np.random.randint(0,300,50)
# print(y)
# print(plt.scatter(x,y))
# print(plt.show())

# #plt.scatter on pandas dataframe
# df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/batter.csv')
# print(df)
# print(df.head(50))
# print(plt.scatter(df['avg'],df['strike_rate']))
# print(plt.show())

# print(plt.scatter(df['avg'],df['strike_rate'],color='pink',marker='*'))
# print(plt.title('Avg and SR analysis of Top 50 batsman'))
# print(plt.xlabel('Average'))
# print(plt.ylabel('SR'))
# print(plt.show())

#size 
tips = sns.load_dataset('tips')
print(tips)
print(plt.scatter(tips['total_bill'],tips['tip'],s=tips['size']*50))
print(plt.show())

#scatter plot using plt.plot
#faster
print(plt.plot(tips['total_bill'],tips['tip'],'o'))
print(plt.show())

