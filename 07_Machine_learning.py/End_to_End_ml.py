import numpy as np 
import pandas as pd

df = pd.read_csv('/Users/aryankasera/Desktop/180-Days-Python/07_Machine_learning.py/placement.csv')
print(df)
print(df.head())

#Steps
# 0. Preprocess + EDA + Feature Selection
# 1. Extract input and output columns
# 2. Scale the values
# 3. Train test split
# 4. Train the model
# 5. Evaluate the model/model selection
# 6. Deploy the model

print(df.info())
# 0. Preprocess + EDA + Feature Selection
df = df.iloc[:,1:]
print(df.head())

import matplotlib.pyplot as plt
print(plt.scatter(df['cgpa'],df['iq'],c=df['placement']))
# print(plt.show())

# 1. Extract input and output columns
X = df.iloc[:,0:2]
y = df.iloc[:,-1]
print(X)
print(y)

# 3. Train test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1)
print(X_train)
print(y_train)
print(X_test)
print(y_test)

# 2. Scale the values
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
print(X_train)

X_test = scaler.transform(X_test)
print(X_test)

# 4. Train the model
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
print(clf.fit(X_train,y_train))

# 5. Evaluate the model/model selection
y_pred = clf.predict(X_test)
print(y_pred)
print(y_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,y_pred))

from mlxtend.plotting import plot_decision_regions
print(plot_decision_regions(X_train,y_train.values,clf=clf,legend = 2))
print(plt.show())

import pickle
print(pickle.dump(clf,open('model.pkl','wb')))