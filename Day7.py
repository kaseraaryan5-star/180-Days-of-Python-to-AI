# "For" loop
nums = [1,2,3,4,5]

for val in nums:
    print(val)

veggies = ["potato", "ladyfinger", "onion", "tomato"]

for val in veggies:
    print(val)

tup = (1,2,3,4,5,4,3,2,1)

for val in tup:
    print(val)

# else in for loop 
str = "ARYAN KASERA"

for char in str:
    print(char)
else:
    print("End of the loop")

# Practice Question 
nums = [1,4,9,16,25,36,49,64,81,100]
for val in nums:
    print(val)

nums = [1,4,9,16,25,36,49,64,81,100]
x = 64 

idx = 0 
for val in nums:
    if(val == x):
        print("number found at idx", idx)
    idx += 1

# Range in for loop 
seq = range(10)

for i in seq:
    print(i)

for i in range(10):
    print(i)

for i in range(2,10):
    print(i)

for i in range(2 ,10 ,2):
    print(i)    

# Practice Question 
for i in range(1, 101):
    print(i)

for i in range(101, 0, -1):
    print(i)

n = int(input("enter number :"))

for i in range(1, 11):
    print(n * i)

# Pass in for loop 
for i in range(5):
    pass

print("some useful work")

# Practice Question
n = 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print("total sum :",sum)

n =  5
fact = 1

for i in range(1, n+1):
    fact *= i

print("factorial", fact)