import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# print(plt.style.use('default'))

# # 2D PLOT 
# #plotting a simple function
# # price = [50000,55000,58000,57000,52000,48000]
# # year = [2026,2027,2028,2029,2030,2031]

# # print(plt.plot(year,price))
# # #print(plt.show())

# #from a pandas dataframe
# batsman = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/sharma-kohli.csv')
# # # print(batsman)
# # plt.plot(batsman['index'],batsman['V Kohli'])
# # # plt.tight_layout()
# # # plt.show()

# # #plotting multiple plots
# # print(plt.plot(batsman['index'],batsman['V Kohli']))
# # print(plt.plot(batsman['index'],batsman['RG Sharma']))
# # print(plt.tight_layout())
# # print(plt.show())

# # #labels plt.title
# # print(plt.plot(batsman['index'],batsman['V Kohli']))
# # print(plt.plot(batsman['index'],batsman['RG Sharma']))

# # print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# # print(plt.xlabel('Season'))
# # print(plt.ylabel('Runs Scored'))
# # print(plt.tight_layout())
# # print(plt.show())

# # colors(hex) 
# # print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue'))
# # print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black'))

# # print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# # print(plt.xlabel('Season'))
# # print(plt.ylabel('Runs Scored'))
# # print(plt.tight_layout())
# # print(plt.show())

# # #line(width and style)
# # print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashed'))
# # print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashed'))

# # print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# # print(plt.xlabel('Season'))
# # print(plt.ylabel('Runs Scored'))
# # print(plt.tight_layout())
# # print(plt.show())

# # print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dotted'))
# # print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dotted'))

# # print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# # print(plt.xlabel('Season'))
# # print(plt.ylabel('Runs Scored'))
# # print(plt.tight_layout())
# # print(plt.show())

# # print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashdot'))
# # print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashdot'))

# # print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# # print(plt.xlabel('Season'))
# # print(plt.ylabel('Runs Scored'))
# # print(plt.tight_layout())
# # print(plt.show())

# # print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashed',linewidth=6))
# # print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashed',linewidth=4))

# # print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# # print(plt.xlabel('Season'))
# # print(plt.ylabel('Runs Scored'))
# # print(plt.tight_layout())
# # print(plt.show())


# # print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashed',linewidth=2,marker='D'))
# # print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashed',linewidth=2,marker='o'))

# # print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# # print(plt.xlabel('Season'))
# # print(plt.ylabel('Runs Scored'))
# # print(plt.tight_layout())
# # print(plt.show())

# #legend -> location 
# # print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashed',linewidth=2,marker='D',label='Virat'))
# # print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashed',linewidth=2,marker='o',label='Rohit'))

# # print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# # print(plt.xlabel('Season'))
# # print(plt.ylabel('Runs Scored'))
# # print(plt.legend())
# # print(plt.tight_layout())
# # print(plt.show())

# # #limiting axis
# # price = [50000,55000,58000,57000,52000,480000]
# # year = [2026,2027,2028,2029,2030,2031]

# # print(plt.plot(year,price))
# # print(plt.ylim(0,100000))
# # print(plt.xlim(2028,2030))
# # print(plt.show())

# #grid
# # print(plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='dashed',linewidth=2,marker='D',label='Virat'))
# # print(plt.plot(batsman['index'],batsman['RG Sharma'],color='black',linestyle='dashed',linewidth=2,marker='o',label='Rohit'))

# # print(plt.title('Rohit Vs Kohli Carrer Comparison'))
# # print(plt.xlabel('Season'))
# # print(plt.ylabel('Runs Scored'))
# # print(plt.legend())
# # print(plt.tight_layout())
# # print(plt.show())
# # print(plt.grid())





# #SCATTER PLOT
# #plt.scatter simple function
# # x = np.linspace(-10,10,50)

# # y = 10*x +3 + np.random.randint(0,300,50)
# # print(y)
# # print(plt.scatter(x,y))
# # print(plt.show())

# # #plt.scatter on pandas dataframe
# # df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/batter.csv')
# # print(df)
# # print(df.head(50))
# # print(plt.scatter(df['avg'],df['strike_rate']))
# # print(plt.show())

# # print(plt.scatter(df['avg'],df['strike_rate'],color='pink',marker='*'))
# # print(plt.title('Avg and SR analysis of Top 50 batsman'))
# # print(plt.xlabel('Average'))
# # print(plt.ylabel('SR'))
# # print(plt.show())

# #size 
# tips = sns.load_dataset('tips')
# print(tips)
# print(plt.scatter(tips['total_bill'],tips['tip'],s=tips['size']*50))
# print(plt.show())

# #scatter plot using plt.plot
# #faster
# print(plt.plot(tips['total_bill'],tips['tip'],'o'))
# print(plt.show())




# # BAR CHART
# #simple bar chart 
# children = [10,20,40,10,30]
# color = ['red','purple','baby pink','blue','yellow']
# print(plt.bar(color,children))
# print(plt.show())

# #horizontal bar chart
# print(plt.barh(color,children))
# print(plt.show())

# #color and label
# df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/batsman_season_record.csv')
# print(df)
# print(plt.bar(df['batsman'],df['2015']))
# print(plt.show())

# #xticks and Multiple bar
# print(plt.bar(np.arange(df.shape[0]) - 0.2,df['2015'],width=0.2))
# print(plt.bar(np.arange(df.shape[0]),df['2016'],width=0.2))
# print(plt.bar(np.arange(df.shape[0]) + 0.2,df['2017'],width=0.2))

# print(plt.xticks(np.arange(df.shape[0]), df['batsman']))
# print(plt.show())

# #a problem 
# children = [10,20,40,10,30]
# colors = ['red red red red','blue blue blue blue','green green green green','yellow yellow yellow yellow','pink pink pink pink']

# print(plt.bar(colors,children,color='pink'))
# print(plt.xticks(rotation='vertical'))
# print(plt.show())

# #stacked bar chart
# print(plt.bar(df['batsman'],df['2017'],label='2017'))
# print(plt.bar(df['batsman'],df['2016'],bottom=df['2017'],label='2016'))
# print(plt.bar(df['batsman'],df['2015'],bottom=(df['2016'] + df['2017']),label='2015'))

# print(plt.legend())
# print(plt.show())




# #HISTOGRAM
# #simple data
# data = [34,54,23,44,55,65,31,77]
# print(plt.hist(data))
# print(plt.show())

# #on some data
# df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/vk.csv')
# print(df)
# print(plt.hist(df['batsman_runs'], bins=[0,10,20,30,40,50,60,70,80,90,100,110,120]))
# print(plt.show())

# #logarithmic scale
# arr = np.load('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/big-array.npy')
# print(plt.hist(arr,bins=[10,20,30,40,50,60,70],log=True))
# print(plt.show())




# # PIE CHART
# #simple data
# data = [32,56,34,76,99]
# subjects = ['eng','physics','sst','sanskrit','maths']
# print(plt.pie(data,labels=subjects))
# print(plt.show())

# #dataset
df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/gayle-175.csv')
# print(df)
# print(plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%'))
# print(plt.show())

#percentage and colors
print(plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%',colors=['blue','pink','purple','red','yellow','brown']))
print(plt.show())

#explode shadow
print(plt.pie(df['batsman_runs'],labels=df['batsman'],autopct='%0.1f%%',explode=[0.6,0,0,0,0,0.10],shadow=True))
print(plt.show())


print(plt.style.use('dark_background'))
# Changing Style
arr = np.load('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/big-array.npy')
print(plt.hist(arr,bins=[10,20,30,40,50,60,70],log=True))
print(plt.show())



# Save Figure
arr = np.load('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/big-array.npy')
print(plt.hist(arr,bins=[10,20,30,40,50,60,70],log=True))
print(plt.savefig('sample.png'))