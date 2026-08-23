import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

tips = sns.load_dataset('tips')
print(tips)

#scatter plot -> axes level function
print(sns.scatterplot(data=tips, x='total_bill',y='tip',hue='sex',style='time',size='size'))
print(plt.show())

#relplot -> figure level function -> square shape
print(sns.relplot(data=tips,x='total_bill',y='tip',kind='scatter',hue='sex',style='time',size='size'))
print(plt.show())


#line plot
gap = px.data.gapminder()
print(gap)
temp_df = gap[gap['country'] == 'India']
print(temp_df)

#axes level function
print(sns.lineplot(data=temp_df,x='year',y='lifeExp'))
print(plt.show())

#using relplot
print(sns.relplot(data=temp_df,x='year',y='lifeExp',kind='line'))
print(plt.show())

#hue -> style
temp_df = gap[gap['country'].isin(['India','Pakistan','China'])]
print(temp_df)
print(sns.relplot(kind='line',data=temp_df,x='year',y='lifeExp',hue='country'))
print(plt.show())

print(sns.lineplot(data=temp_df,x='year',y='lifeExp',hue='country'))
print(plt.show())

#facet plot -> figure level function -> work with relplot
#it will not work with scatter plot and line plot
print(sns.relplot(data=tips,x='total_bill',y='tip',kind='scatter',col='sex'))
print(plt.show())

print(sns.relplot(data=tips,x='total_bill',y='tip',kind='scatter',row='sex'))
print(plt.show())

#col wrap
print(sns.relplot(data=gap,x='lifeExp',y='gdpPercap',kind='scatter',col='year',col_wrap=4))
print(plt.show())




#2. DISTRIBUTION PLOTS
#1.histplot
#2.kdeplot
#3.rugplot
#figure level -> displot
#axes level -> histplot -> kdeplot -> rugplot

#1.plotting univarient histogram
print(sns.histplot(data=tips,x='total_bill'))
print(plt.show())

print(sns.displot(data=tips,x='total_bill',kind='hist'))
print(plt.show())

#bins parameter
print(sns.displot(data=tips,x='total_bill',kind='hist',bins=20))
print(plt.show())

#It's also possible to visualize the distribution of a categorial variable using the logic of histogram
#Discrete bins are automatically set for categorial variables
#countplot
print(sns.displot(data=tips,x='day',kind='hist'))
print(plt.show())

#hue parameter
print(sns.displot(data=tips,x='day',kind='hist',hue='sex'))
print(plt.show())

#element -> step
print(sns.displot(data=tips,x='day',kind='hist',hue='sex',element='step'))
print(plt.show())

#faceting using col and row -> not work on hisplot function
print(sns.displot(data=tips,x='day',kind='hist',col='sex',element='step'))
print(plt.show())


#2.kdeplot
#Rather than using discrete bins, a KDE plot smooths the observations with a Gaussian kernel, producing a continous density estimate
print(sns.kdeplot(data=tips,x='total_bill'))
print(plt.show())

print(sns.displot(data=tips,x='total_bill',kind='kde'))
print(plt.show())

#hue -> fill 
print(sns.displot(data=tips,x='total_bill',kind='kde',hue='sex',fill=True))
print(plt.show())


#3.rugplot
#Plot marignal distributions by drawing ticks along the x and y axes
#This function is intended to complement other plots by showing the location of individual observationn in an unobtrusive way
print(sns.kdeplot(data=tips,x='total_bill'))
print(sns.rugplot(data=tips,x='total_bill'))
print(plt.show())

#Bivariate histogram
#A bivariate histogram bins the data within rectangles that tile the plot
#and then show the count of observations within each reactangle with the fill color
print(sns.histplot(data=tips,x='total_bill',y='tip'))
print(sns.displot(data=tips,x='total_bill',y='tip',kind='hist'))
print(plt.show())

#Bivariant Kdeplot
#a bivariant KDE plot smoothes the (x,y) observations with a 2D Gaussian 
print(sns.kdeplot(data=tips,x='total_bill',y='tip'))
print(plt.show())




# 3. MATRIX PLOT
#1.Heatmap
#2.Clustermap

#1.Heatmap
#Plot rectangular data as a color-encoded matrix
temp_df = gap.pivot(index='country',columns='year',values='lifeExp')

#axes level function
print(plt.figure(figsize=(15,12)))
print(sns.heatmap(temp_df))
print(plt.show())

#annot
temp_df = gap[gap['continent'] == 'Europe'].pivot(index='country',columns='year',values='lifeExp')
print(plt.figure(figsize=(15,12)))
print(sns.heatmap(temp_df,annot=True,linewidths=0.8,cmap='winter'))
print(plt.show())


#2.Clustermap
#Plot a matrix dataset as a hierarchically-clustered heatmap
#This fuction requires scipy to be available
iris = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/06_Data_Visualisation/iris.csv')
print(iris.sample(5))
print(px.data.iris())

print(sns.clustermap(iris.iloc[:,[0,1,2,3]]))
print(plt.show())
