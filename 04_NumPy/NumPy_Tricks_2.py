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