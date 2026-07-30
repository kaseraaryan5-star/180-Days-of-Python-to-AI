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



#Changing Datatypes
#astype
a = a1.astype(np.int32)
print(a)
b = a2.astype(np.int32)
print(b)
c = a3.astype(np.int32)
print(c)



#Array Operations
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)
print(a1)
print(a2)

#scalar operation
#arithmetic
a = a1*2
print(a)
b = a2**2
print(b)

#vector operation
#arithmetic
c = a1 * a2
print(c)
d = a1 / a2
print(d)

#relational
e =a2 > 5
print(e)
f = a1 < 8
print(f)



#Array Functions
a1 = np.random.random((3,3))
a1 = np.round(a1*100)
print(a1)

#0 -> column and 1 -> row
#max/min/sum/prod
a = np.max(a1)
print(a)
b = np.min(a1)
print(b)
c = np.sum(a1)
print(c)
d = np.prod(a1)
print(d)
e = np.max(a1,axis=1)
print(e)
f = np.prod(a1,axis=0)
print(f)

#mean/median/std/var
a = np.mean(a1,axis=0)
print(a)
b = np.median(a1,axis=1)
print(b)
c = np.std(a1,axis=0)
print(c)
d = np.var(a1,axis=1)
print(d)

#trigonometric functions
a = np.tan(a1)
print(a)

#dot product
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)
a = np.dot(a2,a3)
print(a)

#log and exponents
a = np.log(a1)
print(a)
b = np.exp(a1)
print(b)

#round/floor/ceil
a = np.round(np.random.random((2,3))*100)
print(a)
b = np.floor(np.random.random((2,3))*100)
print(b)
c = np.ceil(np.random.random((2,3))*100)
print(c)



#Indexing and Slicing
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

#indexing
a = a1[2]
print(a)
b = a2[1,0]
print(b)
c = a3[0,1,0]
print(c)

#slicing
d = a1[2:5]
print(d)
e = a2[:,0]
print(e)
f = a3[::2]
print(f)



#Iterating
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)
for i in a1:
    print(i)
for i in a2:
    print(i)
for i in a3:
    print(i)
for i in np.nditer(a3):
    print(i)



#Reshaping
#transpose
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)
a = a1.T
print(a)
b = a2.T
print(b)
c = a3.T
print(c)

#ravel
a = a1.ravel()
print(a)
b = a2.ravel()
print(b)
c = a3.ravel()
print(c)



#Stacking
a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)

#horizontal stacking
a = np.hstack((a4,a5,a4,a5,a4,a5))
print(a)

#vertical stacking
b = np.vstack((a4,a5,a4,a5))
print(b)



#Spliting
a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)

#horizontal spliting
a = np.hsplit(a4,2)
print(a)

#vertical spliting
b = np.vsplit(a5,3)
print(b)

