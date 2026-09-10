from sklearn.datasets import make_classification
import numpy as np
import matplotlib.pyplot as plt

# 1. Dataset create karna
X, y = make_classification(n_samples=100, n_features=2, n_informative=1, n_redundant=0, 
                           n_classes=2, n_clusters_per_class=1, random_state=41, hypercube=False, class_sep=10)

# 2. Shuruat me data points ko plot karna (Jo aapne pehle kiya tha)
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='winter', s=100)
print(plt.show())

# 3. Perceptron algorithm function
def perceptron(X, y):
    X = np.insert(X, 0, 1, axis=1) # Bias term (X0 = 1) add karna
    weights = np.ones(X.shape[1])  # X.shape[1] se sahi weights matrix banegi
    lr = 0.1
    
    # Activation function
    def step(z):
        return 1 if z >= 0 else 0
    
    # Training Loop
    for i in range(1000):
        j = np.random.randint(0, 100)
        y_hat = step(np.dot(X[j], weights)) # Yahan se 'plt.' hata diya hai
        weights = weights + lr * (y[j] - y_hat) * X[j]
        
    return weights[0], weights[1:]

# 4. Function ko call karna
intercept_, coef_ = perceptron(X, y)

# 5. Decision Boundary (Line) ko graph par plot karna
# Line ki equation: w1*x1 + w2*x2 + bias = 0 => x2 = -(w1/w2)*x1 - (bias/w2)
m = -(coef_[0] / coef_[1])
c = -(intercept_ / coef_[1])

x_input = np.linspace(-3, 3, 100)
y_input = m * x_input + c

plt.plot(x_input, y_input, color='red', linewidth=3)
plt.ylim(-3, 3) # Graph ko sahi se scale karne ke liye
plt.show()

m = -(coef_[0]/coef_[1])
b = -(intercept_/coef_[1])
x_input = np.linspace(-3,3,100)
y_input = m*x_input + b
plt.figure(figsize=(10,6))
plt.plot(x_input,y_input,color='red',linewidth=3)
plt.scatter(X[:,0],X[:,1],c=y,cmap='winter',s=100)
plt.ylim(-3,2)
print(plt.show())