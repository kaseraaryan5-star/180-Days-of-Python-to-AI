import pandas as pd
import numpy as np

import scipy.stats as stats

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import pipeline
from sklearn import pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer

df = pd.read_csv('/Users/aryankasera/Desktop/100-Days-AI/07_Machine_learning.py/train.csv',usecols=['Age','Fare','Survived'])
print(df.head())
print(df.isnull().sum())

df['Age'].fillna(df['Age'].mean(),inplace=True)
print(df.head())

X = df.iloc[:,1:3]
y = df.iloc[:,0]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

plt.figure(figsize=(14,4))
plt.subplot(121)
sns.kdeplot(X_train['Age'])
plt.title('Age PDF')

plt.subplot(122)
stats.probplot(X_train['Age'], dist="norm", plot=plt)
plt.title('Age QQ Plot')

print(plt.show())

plt.figure(figsize=(14,4))
plt.subplot(121)
sns.kdeplot(X_train['Fare'])
plt.title('Fare PDF')

plt.subplot(122)
stats.probplot(X_train['Fare'], dist="norm", plot=plt)
plt.title('Fare QQ Plot')

print(plt.show())

clf = LogisticRegression(solver='saga')
clf2 = DecisionTreeClassifier()

from sklearn.impute import SimpleImputer

# Imputer banayein jo missing values ko 'mean' se bhar de
imputer = SimpleImputer(strategy='mean')

# X_train aur X_test par fit_transform/transform apply karein
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

clf.fit(X_train,y_train)
clf2.fit(X_train,y_train)
    
y_pred = clf.predict(X_test)
y_pred1 = clf2.predict(X_test)
    
print("Accuracy LR",accuracy_score(y_test,y_pred))
print("Accuracy DT",accuracy_score(y_test,y_pred1))

trf = FunctionTransformer(func=np.log1p)
X_train_transformed = trf.fit_transform(X_train)
X_test_transformed = trf.transform(X_test)

clf = LogisticRegression(solver='saga')
clf2 = DecisionTreeClassifier()

clf.fit(X_train_transformed,y_train)
clf2.fit(X_train_transformed,y_train)
    
y_pred = clf.predict(X_test_transformed)
y_pred1 = clf2.predict(X_test_transformed)
    
print("Accuracy LR",accuracy_score(y_test,y_pred))
print("Accuracy DT",accuracy_score(y_test,y_pred1))

X_transformed = trf.fit_transform(X)

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
X_transformed = imputer.fit_transform(X_transformed)

clf = LogisticRegression(solver='saga')
clf2 = DecisionTreeClassifier()

print("LR",np.mean(cross_val_score(clf,X_transformed,y,scoring='accuracy',cv=10)))
print("DT",np.mean(cross_val_score(clf2,X_transformed,y,scoring='accuracy',cv=10)))

plt.figure(figsize=(14,4))

plt.subplot(121)
stats.probplot(X_train[:,1], dist="norm", plot=plt)
plt.title('Fare Before Log')

plt.subplot(122)
stats.probplot(X_train_transformed[:,1], dist="norm", plot=plt)
plt.title('Fare After Log')

print(plt.show())

plt.figure(figsize=(14,4))

plt.subplot(121)
stats.probplot(X_train[:,0], dist="norm", plot=plt)
plt.title('Age Before Log')

plt.subplot(122)
stats.probplot(X_train_transformed[:,0], dist="norm", plot=plt)
plt.title('Age After Log')

print(plt.show())

# Agar 'Fare' ka index 1 hai, toh aise likho:
trf2 = ColumnTransformer([
    ('log', FunctionTransformer(np.log1p), [1])  # 'Fare' ki jagah index [1] ya jo bhi index ho wo likhein
], remainder='passthrough')

X_train_transformed2 = trf2.fit_transform(X_train)
X_test_transformed2 = trf2.transform(X_test)

clf = LogisticRegression(solver='saga')
clf2 = DecisionTreeClassifier()

clf.fit(X_train_transformed2,y_train)
clf2.fit(X_train_transformed2,y_train)
    
y_pred = clf.predict(X_test_transformed2)
y_pred2 = clf2.predict(X_test_transformed2)
    
print("Accuracy LR",accuracy_score(y_test,y_pred))
print("Accuracy DT",accuracy_score(y_test,y_pred2))

X_transformed2 = trf2.fit_transform(X)
X_transformed2 = imputer.fit_transform(X_transformed2)  # Yeh line zaroor add karein!
# Agar 'Fare' ka index 1 hai, toh aise likho:
trf2 = ColumnTransformer([
    ('log', FunctionTransformer(np.log1p), [1])  # 'Fare' ki jagah index [1] ya jo bhi index ho wo likhein
], remainder='passthrough')
clf = LogisticRegression(solver='saga')
clf2 = DecisionTreeClassifier()

print("LR",np.mean(cross_val_score(clf,X_transformed2,y,scoring='accuracy',cv=10)))
print("DT",np.mean(cross_val_score(clf2,X_transformed2,y,scoring='accuracy',cv=10)))

def apply_transform(transform):
    X = df.iloc[:, 1:3]
    y = df.iloc[:, 0]
    
    trf = ColumnTransformer([
        ('log', FunctionTransformer(transform), ['Fare'])
    ], remainder='passthrough')
    
    X_trans = trf.fit_transform(X)
    
    # Yeh imputer wali line zaroor add kar do:
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(strategy='mean')
    X_trans = imputer.fit_transform(X_trans)
    
    clf = LogisticRegression(solver='saga')
    
    print("Accuracy", np.mean(cross_val_score(clf, X_trans, y, scoring='accuracy', cv=10)))
    
    plt.figure(figsize=(14,4))
    # (baaki ka graph wala code waise hi rahega)
    
    plt.subplot(121)
    stats.probplot(X['Fare'], dist="norm", plot=plt)
    plt.title('Fare Before Transform')

    plt.subplot(122)
    stats.probplot(X_trans[:,0], dist="norm", plot=plt)
    plt.title('Fare After Transform')

print(plt.show())
print(apply_transform(np.sin))