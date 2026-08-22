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
# print(batters.head())
# print(plt.figure(figsize=(15,6)))
# print(plt.scatter(batters['avg'],batters['strike_rate']))
# print(plt.title('Something'))
# print(plt.xlabel('Avg'))
# print(plt.ylabel('Strike Rate'))
# print(plt.show())

# fig,ax = plt.subplots(figsize=(15,6))
# print(fig,ax)
# print(ax.scatter(batters['avg'],batters['strike_rate']))
# print(ax.set_title('Something'))
# print(ax.set_xlabel('Avg'))
# print(ax.set_ylabel('Strike Rate'))
# print(fig.show())

# #batter dataset
# print(plt.subplots(nrows=2,ncols=2))
# print(plt.show())

# print(plt.subplots(nrows=5,ncols=5))
# print(plt.show())

# fig,ax = plt.subplots(nrows=2,ncols=1,sharex=True,figsize=(15,8))

# print(ax[0].scatter(batters['avg'],batters['strike_rate'],color='red'))
# print(ax[1].scatter(batters['avg'],batters['runs']))

# print(ax[0].set_title('Avg Vs Strike Rate'))
# print(ax[1].set_title('Strike Rate'))

# print(ax[1].set_title('Avg Vs Runs'))
# print(ax[1].set_ylabel('Runs'))
# print(ax[1].set_xlabel('Avg'))
# print(plt.show())




# 3D SCATTER PLOT
# print(batters)
# fig = plt.figure()
# ax = plt.subplot(projection='3d')
# print(ax)

# print(ax.scatter3D(batters['runs'],batters['avg'],batters['strike_rate']))
# print(ax.set_title('IPL batsman analysis'))
# print(ax.set_xlabel('Runs'))
# print(ax.set_ylabel('Avg'))
# print(ax.set_zlabel('SR'))
# print(plt.show())




# # 3D LINE PLOT
# x = [0,1,5,25]
# y = [0,10,13,0]
# z = [0,13,20,9]

# fig = plt.figure()
# ax = plt.subplot(projection='3d')
# print(ax.scatter3D(x,y,z,s=[100,100,100,100]))
# print(ax.plot3D(x,y,z,color='red'))
# print(plt.show())




# # # 3D SURFACE PLOTS
# x = np.linspace(-10,10,100)
# y = np.linspace(-10,10,100)
# xx, yy = np.meshgrid(x,y)

# z = xx**2 + yy**2
# # print(z.shape)

# # fig = plt.figure(figsize=(12,8))
# # ax = plt.subplot(projection='3d')
# # p = ax.plot_surface(xx,yy,z,cmap='viridis')
# # print(p)
# # print(fig.colorbar(p))
# # print(plt.show())


# # # 2nd 
# # z = np.sin(xx)+ np.cos(yy)
# # fig = plt.figure(figsize=(12,8))
# # ax = plt.subplot(projection='3d')
# # p = ax.plot_surface(xx,yy,z,cmap='viridis')
# # print(p)
# # print(fig.colorbar(p))
# # print(plt.show())


# # 3rd 
# z = np.sin(xx) + np.log(yy)
# fig = plt.figure(figsize=(12,8))
# ax = plt.subplot(projection='3d')
# p = ax.plot_surface(xx,yy,z,cmap='viridis')
# print(p)
# print(fig.colorbar(p))
# print(plt.show())




# # CONTOUR PLOTS
# fig = plt.figure(figsize=(12,8))
# ax = plt.subplot()
# p = ax.contour(xx,yy,z,cmap='viridis')
# print(p)
# print(fig.colorbar(p))
# print(plt.show())


# fig = plt.figure(figsize=(12,8))
# ax = plt.subplot()
# p = ax.contour(xx,yy,z,cmap='viridis')
# print(p)
# print(fig.colorbar(p))
# print(plt.show())




# # HEATMAP
# delivery = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/IPL_Ball_by_Ball_2008_2022.csv')
# print(delivery.head())

# temp_df = delivery[(delivery['ballnumber'].isin([1,2,3,4,5,6])) & (delivery['batsman_run'] == 6)]
# grid = temp_df.pivot_table(index='overs',columns='ballnumber',values='batsman_run',aggfunc='count')

# print(plt.figure(figsize=(20,10)))
# print(plt.imshow(grid))
# print(plt.yticks(delivery['overs'].unique(), list(range(1,21))))
# print(plt.xticks(np.arange(0,6), list(range(1,7))))
# print(plt.colorbar())
# print(plt.show())




# PANDAS PLOT
#on a series
s = pd.Series([1,2,3,4,5,6,7])
print(s.plot(kind='pie'))
print(plt.show())

#can be used dataframe as well
import seaborn as sns
tips = sns.load_dataset('tips')
tips['size'] = tips['size'] * 100
print(tips.head())

# scatter plot -> labels -> markers -> figsize -> color -> cmap
print(tips.plot(kind='scatter',x='total_bill',y='tip',title='Cost analysis',marker='+',figsize=(10,6),s='size',c='sex',cmap='viridis'))
print(plt.show())