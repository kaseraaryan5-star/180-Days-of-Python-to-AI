import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#COLORED SCATTER PLOT
# iris = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/iris.csv')
# print(iris.sample(5))

# iris['Species'] = iris['Species'].replace({'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2})
# print(iris.sample(5))

# print(plt.scatter(iris['SepalLengthCm'],iris['PetalLengthCm'],c=iris['Species'],cmap='jet',alpha=0.9))
# print(plt.xlabel('Sepal length'))
# print(plt.ylabel('Petal length'))
# print(plt.colorbar())
# print(plt.show())


# #Plot size
# print(plt.figure(figsize=(15,7)))

# print(plt.scatter(iris['SepalLengthCm'],iris['PetalLengthCm'],c=iris['Species'],cmap='jet',alpha=0.9))
# print(plt.xlabel('Sepal length'))
# print(plt.ylabel('Petal length'))
# print(plt.colorbar())
# print(plt.show())


# #Annotations
batters = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/batter.csv')
# print(batters.shape)

# sample_df = batters.head(100).sample(25,random_state=5)
# print(sample_df)

# print(plt.figure(figsize=(15,7)))
# print(plt.scatter(sample_df['avg'],sample_df['strike_rate'],s=sample_df['runs']))
# for i in range(sample_df.shape[0]):
#     print(plt.text(sample_df['avg'].values[i],sample_df['strike_rate'].values[i],sample_df['batter'].values[i]))
# print(plt.show())


# x = [1,2,3,4]
# y = [5,6,7,8]

# print(plt.scatter(x,y))
# print(plt.text(1,5,'Point1'))
# print(plt.text(2,6,'Point2'))
# print(plt.text(3,7,'Point3'))
# print(plt.text(4,8,'Point4',fontdict={'size':12,'color':'pink'}))
# print(plt.show())

# #Horizontal and Vertical line
# print(plt.figure(figsize=(15,7)))
# print(plt.scatter(sample_df['avg'],sample_df['strike_rate'],s=sample_df['runs']))
# print(plt.axhline(130,color='red'))
# print(plt.axhline(140,color='black'))
# print(plt.axvline(30,color='pink'))
# for i in range(sample_df.shape[0]):
#     print(plt.text(sample_df['avg'].values[i],sample_df['strike_rate'].values[i],sample_df['batter'].values[i]))
# print(plt.show())




# #SUB PLOT
#a different way to plot graphs
print(batters.head())
print(plt.figure(figsize=(15,6)))
print(plt.scatter(batters['avg'],batters['strike_rate']))
print(plt.title('Something'))
print(plt.xlabel('Avg'))
print(plt.ylabel('Strike Rate'))
print(plt.show())

fig,ax = plt.subplots(figsize=(15,6))
print(fig,ax)
print(ax.scatter(batters['avg'],batters['strike_rate']))
print(ax.set_title('Something'))
print(ax.set_xlabel('Avg'))
print(ax.set_ylabel('Strike Rate'))
print(fig.show())

#batter dataset
print(plt.subplots(nrows=2,ncols=2))
print(plt.show())

print(plt.subplots(nrows=5,ncols=5))
print(plt.show())

fig,ax = plt.subplots(nrows=2,ncols=1,sharex=True,figsize=(15,8))

print(ax[0].scatter(batters['avg'],batters['strike_rate'],color='red'))
print(ax[1].scatter(batters['avg'],batters['runs']))

print(ax[0].set_title('Avg Vs Strike Rate'))
print(ax[1].set_title('Strike Rate'))

print(ax[1].set_title('Avg Vs Runs'))
print(ax[1].set_ylabel('Runs'))
print(ax[1].set_xlabel('Avg'))
print(plt.show())

