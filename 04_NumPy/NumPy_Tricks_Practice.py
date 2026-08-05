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

import numpy as np

a = np.random.randint(1,100,15)
b = np.random.randint(1,100,24).reshape(6,4)
print(a)
print(b)

#np.histogram
#NumPy has a built-in numpy.histogram() function which represents the frequency of data distribution in the graphical form
a1 = np.histogram(a,bins=[0,50,100])
print(a1)

#np.corrcoef
#Return Pearson product-moment correlation coefficients
salary = np.array([20000,40000,25000,35000,60000])
experience = np.array([1,3,2,4,2])
i = np.corrcoef(salary,experience)
print(i)

#np.isin
#With the help of numpy.isin() method, we can see that one array having values are checked in a different numpy array having different elements with differemt sizes
items = [10,20,30,40,50,60,70,80,90,100]
a1 = a[np.isin(a,items)]
print(a1)

#np.flip
#The numpy.flip() function reverses the order of array elements along the specified axis preserving the shape of the array
a1 = np.flip(a)
print(a)
print(a1)                              

#np.put
#The numpy.put() function replaces specific elements of an array with given values of p_array. Array indexed works on flattened array
a1 = np.put(a,[0,1],[1100,53000000])
print(a1)

#np.delete 
#The numpy.delete() function returns a new array with the deletion of sub-arrays along with the mentioned axis
a1 = np.delete(a,[0,2,4])
print(a1)



#Set Function
m = np.array([1,2,3,4,5,6,7])
n = np.array([3,4,5,6,7,8,])

#np.union1d
a1 = np.union1d(m,n)
print(a1)

#np.intersect1d
a1 = np.intersect1d(m,n)
print(a1)

#np.setdiff1d
a1 = np.setdiff1d(m,n)
print(a1)

#np.setxor1d
a1 = np.setxor1d(m,n)
print(a1)

#np.clip
#numpy.clip() function is used to Clip(limit) the values in an array
a1 = np.clip(a,a_min=25,a_max=75)
print(a1)