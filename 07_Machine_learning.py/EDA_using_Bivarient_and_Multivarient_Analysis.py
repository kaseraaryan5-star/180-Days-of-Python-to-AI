import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
print(tips)

titanic = pd.read_csv('/Users/aryankasera/Desktop/100-Days-AI/07_Machine_learning.py/train.csv')
print(titanic)

flights = sns.load_dataset('flights')
print(flights)

iris = sns.load_dataset('iris')
print(iris)

# 1.Scatterplot (Numerical - Numerical)
print(sns.scatterplot(x=tips['total_bill'],y=tips['tip'],hue=tips['sex'],style=tips['smoker'],size=tips['size']))
print(plt.show())

# 2.Barplot (Numerical - Categorical)
print(titanic.head())
print(sns.barplot(x=titanic['Pclass'],y=titanic['Age']))
print(plt.show())

print(sns.barplot(x=titanic['Pclass'],y=titanic['Fare']))
print(plt.show())

print(sns.barplot(x=titanic['Pclass'],y=titanic['Age'],hue=titanic['Sex']))
print(plt.show())

print(sns.barplot(x=titanic['Pclass'],y=titanic['Fare'],hue=titanic['Sex']))
print(plt.show())

# 3.Boxplot (Numerical - Categorical)
print(sns.boxplot(x=titanic['Sex'],y=titanic['Age'],hue=titanic['Survived']))
print(plt.show())

# 4.KDE plot (Numerical - Categorical)
print(sns.kdeplot(data=titanic,x='Age',hue='Survived',fill=True))
print(plt.show())

# 5.Heatmap (Categorical - Categorical)
print(titanic.head(3))
print(pd.crosstab(titanic['Pclass'],titanic['Survived']))
print(sns.heatmap(pd.crosstab(titanic['Pclass'],titanic['Survived'])))
print(plt.show())

print(titanic.groupby('Pclass').mean(numeric_only=True)['Survived']*100)

print((titanic.groupby('Pclass').mean(numeric_only=True)['Survived']*100).plot(kind='bar'))
print(plt.show())

# 6.Clustermap (Categorical - Categorical)
print(pd.crosstab(titanic['SibSp'],titanic['Survived']))
print(sns.clustermap(pd.crosstab(titanic['SibSp'],titanic['Survived'])))
print(plt.show())

print(sns.clustermap(pd.crosstab(titanic['Parch'],titanic['Survived'])))
print(plt.show())

# 7.Pairplot
print(iris.head())
print(sns.pairplot(iris,hue='species'))
print(plt.show())

# 8.Lineplot (Numerical - Numerical)
print(flights.head())
new = flights.groupby('year').sum(numeric_only=True).reset_index()
print(new)

print(sns.lineplot(x=new['year'],y=new['passengers']))
print(plt.show())

print(flights.pivot_table(values='passengers',index='month',columns='year'))
print(sns.heatmap(flights.pivot_table(values='passengers',index='month',columns='year')))
print(plt.show())

print(sns.clustermap(flights.pivot_table(values='passengers',index='month',columns='year')))
print(plt.show())

