import numpy as np

a = np.random.randint(1,100,15)
b = np.random.randint(1,100,24).reshape(6,4)
print(a)
print(b)

#np.sort
#Return a sorted copy of an array
a1 = np.sort(a)
a2 = np.sort(b)
print(a1)
print(a2)

#np.append
#The numpy.append()appends values along the mentioned axis at the end of the array
a1 = np.append(a,200)
a2 = np.append(b,np.ones((b.shape[0],1)),axis=1)
print(a1)
print(a2)

#np.concatenate
#numpy.concatenate() function concatenate a sequences of arrays along an existing axis
c = np.arange(6).reshape(2,3)
d = np.arange(6,12).reshape(2,3)
print(c)
print(d)
c1 = np.concatenate((c,d),axis=0)
print(c1)
d1 = np.concatenate((c,d),axis=1)
print(d1)

#np.unique
#With the helpof np.unique() method, we can get the unique values from an array given as parameter in np.unique() method
e = np.array([1,2,1,2,3,4,3,2,2,3,4,3,2,5,6,7,8,7,6,5,5,6,7,8,6,6,5])
e1 = np.unique(e)
print(e1)

#np.expand_dims 
#With the help of NumPy.expand_dims() method, we can get the expanded dimensions of an array
a1 = np.expand_dims(a,axis=0)
print(a1)

#np.where
#The numpy.where() function returns the indices of elements in a input array where the given condition is satisfied
print(a)
#find all indices with values greater than 50
a1 = np.where(a>50)
print(a1)
#replace all values > 50 with 0
a2 = np.where(a>50,0,a)
print(a2)

#np.argmax
#The numpy.argmax() function returns indices of the max element of the array in a particular axis
a1 = np.argmax(a)
print(a1)

#np.argmin
a1 = np.argmin(a)
print(a1)

#np.cumsum
#numpy.cumsum() function is used when we want to compute the cumulative sum of array elements over a given axis
a1 = np.cumsum(a)
print(a1)
b1 = np.cumsum(b,axis=1)
print(b1)

#np.cumprod
a1 = np.cumprod(a)
print(a1)
b1 = np.cumprod(b)
print(b1)

#np.percentile
#numpy.percentile() function used to compute the nth percentile of the given data (array elements) along the specified axis
a1 = np.percentile(a,59)
print(a1)

