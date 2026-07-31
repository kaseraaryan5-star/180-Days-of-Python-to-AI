# NumPy Array Vs Python Lists


#Speed
#python list
a = [i for i in range(10000000)]
b = [i for i in range(10000000,20000000)]
c = []

import time
start = time.time()
for i in range(len(a)):
    c.append(a[i] + b[i])

print((time.time()-start))

#numpy
import numpy as np
a = np.arange(10000000)
b = np.arange(10000000,20000000)

start = time.time()
c = a + b
print(time.time()-start)


#Memory
# python list
a = [i for i in range(10000000)]
import sys
print(sys.getsizeof(a))

#numpy
a = np.arange(10000000)
print(sys.getsizeof(a))


#Advanced Indexing 
a = np.arange(24).reshape(6,4)
print(a)

#fancy indexing
print(a[[0,2]])
print(a[:,[0,3]])

#Boolean Indexing 
a = np.random.randint(1,100,24).reshape(6,4)
print(a)

#find all numbers greater than 50
print(a[a > 50])
#find out even numbers 
print(a[a % 2 == 0])
#find all numbers greater than 50 and are even
print(a[(a > 50) & (a % 2 == 0)])
#find all numbers divisible by 7
print(a[a % 7 != 0])



#Broadcasting
#same shape
a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)

print(a)
print(b)
print(a + b)

#different shape
a = np.arange(6).reshape(2,3)
b = np.arange(3).reshape(1,3)

print(a)
print(b)
print(a + b)

#more examples
a = np.arange(12).reshape(4,3)
b = np.arange(3)
print(a+b)

a = np.arange(12).reshape(3,4)  #Gives Error
b = np.arange(3)
print(a + b)

a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(3,1)
print(a+b)

a = np.arange(3).reshape(1,3)  #Gives Error
b = np.arange(3).reshape(4,1)
print(a+b)

a = np.array([1])
b = np.arange(4).reshape(2,2)
print(a+b)

a = np.arange(12).reshape(3,4)  #Gives Error
b = np.arange(3).reshape(4,3)
print(a+b)

a = np.arange(16).reshape(4,4)  #Gives Error
b = np.arange(3).reshape(2,2)
print(a+b)




# Working with Mathematical Formulas
a = np.arange(10)
print(a)

#sigmoid
def sigmoid(array):
    return 1/(1 + np.exp(-(array)))

print(sigmoid(a))

#mean squared error
actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)

def mse(actual,predicted):
    return np.mean((actual-predicted)**2)

print(mse(actual,predicted))



#Working with missing values
#np.nan
a = np.array([1,2,3,4,5,np.nan,7])
print(a)
print(a[~np.isnan(a)])



#Plotting Graphs
#plotting a 2D graph
#x = y
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
y = x
print(plt.plot(x,y))
plt.show()

# y = x^2
y = x**2
print(plt.plot(x,y))
plt.show()

# y = sin(x)
y = np.sin(x)
print(plt.plot(x,y))
plt.show()

# y = xlog(x)
y = x * np.log(x)
print(plt.plot(x,y))
plt.show()

#sigmoid
y = 1/(1+np.exp(-x))
print(plt.plot(x,y))
plt.show()

