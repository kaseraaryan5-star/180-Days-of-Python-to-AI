import numpy as np

#Creating Numpy Arrays

#1d type array
a = np.array([1, 2, 3])
print(a)
print(type(a))

#2d type array
b = np.array([[1,2,3],[6,7,8]])
print(b)
print(type(b))

#3d type array
c = np.array([[[1,4,7,],[6,3,8,],[4,8,0,]]])
print(c)
print(type(c))

#dtype array
d = np.array([5,3,7,8], dtype = float)
print(d)

d = np.array([5,3,7,8], dtype = bool)
print(d)

d = np.array([5,3,7,8], dtype = complex)
print(d)

#np.arange
e = np.arange(1,100,3)
print(e)

f = np.arange(2,90)
print(f)

# np.reshape
g = np.arange(1,13).reshape(6,2)
print(g)

#np.ones
h = np.ones((3,4))
print(h)

#np.zeros
i = np.zeros((3,4))
print(i)

#np.random
j = np.random.random((3,4))
print(j)

#np.linspace
k = np.linspace(-10,20,15)
print(k)

#np.identity
l = np.identity(3)
print(l)



#Array Attributes
a1 = np.arange(10)
a2 = np.arange(12, dtype = float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)
print(a1)
print(a2)
print(a3)

#ndim (find dimension)
a = a1.ndim
b = a2.ndim
c = a3.ndim
print(a)
print(b)
print(c)

#shape
a = a1.shape
b = a2.shape
c = a3.shape
print(a)
print(b)
print(c)

#size
a = a1.size
b = a2.size
c = a3.size
print(a)
print(b)
print(c)

#itemsize
a = a1.itemsize
b = a2.itemsize
c = a3.itemsize
print(a)
print(b)
print(c)

#dtype 
a = a1.dtype
b = a2.dtype
c = a3.dtype
print(a)
print(b)
print(c)