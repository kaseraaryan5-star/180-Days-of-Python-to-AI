import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import ssl

# Create an unverified SSL context
ssl._create_default_https_context = ssl._create_unverified_context

#import dataset
tips = sns.load_dataset('tips')
print(tips)

iris = sns.load_dataset('iris')
print(iris)

# CATEGORICAL SCATTER PLOTS
#scatter plot -> axes level function
print(sns.scatterplot(data=tips,x='total_bill',y='tip'))
print(plt.show())

#strip plot 
#axes level function
print(sns.stripplot(data=tips,x='day',y='total_bill'))
print(plt.show())

#using catplot
#figure level function
print(sns.catplot(data=tips,x='day',y='total_bill',kind='strip'))
print(plt.show())

#jitter
print(sns.catplot(data=tips,x='day',y='total_bill',kind='strip',jitter=0.2,hue='sex'))
print(plt.show())

#swarmplot
print(sns.swarmplot(data=tips,x='day',y='total_bill'))
print(plt.show())

print(sns.catplot(data=tips,x='day',y='total_bill',kind='swarm',hue='sex'))
print(plt.show())



# CATEGORICAL DISTRIBUTION PLOT
#Box plot
#axes level function
print(sns.boxplot(data=tips,x='day',y='total_bill'))
print(plt.show())

print(sns.catplot(data=tips,x='day',y='total_bill',kind='box',hue='sex'))
print(plt.show())

#single boxplot -> numerical col
print(sns.boxplot(data=tips,y='total_bill'))
print(plt.show())

# Violin plot - (Boxplot + KDEplot)
print(sns.violinplot(data=tips,x='day',y='total_bill'))
print(plt.show())

print(sns.catplot(data=tips,x='day',y='total_bill',kind='violin',hue='sex',split=True))
print(plt.show())




# CATEGORICAL ESTIMATE PLOT
# bar plot 
import numpy as np 
print(sns.barplot(data=tips,x='day',y='total_bill',hue='smoker',estimator=np.mean))
print(plt.show())

#point plot 
print(sns.pointplot(data=tips,x='day',y='total_bill',hue='smoker'))
print(plt.show())

#count plot 
print(sns.countplot(data=tips,x='sex',hue='day'))
print(plt.show())

#faceting using catplot
print(sns.catplot(data=tips,x='day',y='total_bill',col='smoker',kind='bar',row='time'))
print(plt.show())




# REGRESSION PLOT
print(sns.regplot(data=tips,x='total_bill',y='tip'))
print(plt.show())

print(sns.lmplot(data=tips,x='total_bill',y='tip',hue='sex'))
print(plt.show())

#residplot
print(sns.residplot(data=tips,x='total_bill',y='tip'))
print(plt.show())




# FACET GRID
# figure level -> relplot -> displot -> catplot ->lmplot
print(sns.catplot(data=tips,x='sex',y='total_bill',kind='violin',col='day',row='time'))
print(plt.show())

g = sns.FacetGrid(data=tips,col='day',row='time',hue='smoker')
g.map(sns.scatterplot,'sex','total_bill')
print(g.add_legend())
print(plt.show())

# PairGrid Vs Pairplot
print(sns.pairplot(iris,hue='species'))
print(plt.show())

g = sns.PairGrid(data=iris,hue='species')
print(g.map(sns.scatterplot))
print(plt.show())

# map_diag -> map_offdiag
g = sns.PairGrid(data=iris,hue='species')
print(g.map_diag(sns.boxplot))
print(g.map_offdiag(sns.histplot))

# map_diag -> map_upper -> map_lower
g = sns.PairGrid(data=iris,hue='species')
print(g.map_diag(sns.histplot))
print(g.map_upper(sns.kdeplot))
print(g.map_lower(sns.scatterplot))

#vars
g = sns.PairGrid(data=iris,hue='species',vars=['sepal_width','petal_width'])
print(g.map_diag(sns.histplot))
print(g.map_upper(sns.kdeplot))
print(g.map_lower(sns.scatterplot))


# JointGrid Vs Jointplot 
print(sns.jointplot(data=tips,x='total_bill',y='tip',kind='scatter'))
print(plt.show())

print(sns.jointplot(data=tips,x='total_bill',y='tip',kind='kde'))
print(plt.show())

print(sns.jointplot(data=tips,x='total_bill',y='tip',kind='hist'))
print(plt.show())

print(sns.jointplot(data=tips,x='total_bill',y='tip',kind='resid'))
print(plt.show())


g = sns.JointGrid(data=tips,x='total_bill',y='tip')
print(g.plot(sns.scatterplot,sns.histplot))

g = sns.JointGrid(data=tips,x='total_bill',y='tip')
print(g.plot(sns.scatterplot,sns.boxplot))

g = sns.JointGrid(data=tips,x='total_bill',y='tip')
print(g.plot(sns.kdeplot,sns.histplot))


#Utility fuctions
#get datasets name
print(sns.get_dataset_names)

#load dataset
print(sns.load_dataset('flights'))