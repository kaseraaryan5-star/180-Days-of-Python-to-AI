#CH - 6 (function and Recursion)

# Function
def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum 

calc_sum(5, 10)

# some code lines


calc_sum(2, 10)

# some code lines

calc_sum(12, 17)

# Function definition 
def calc_sum(a, b):  # a and b are called parameters
    return a + b

sum = calc_sum(1, 2)  # function call or 1 and 2 are called arguments
print(sum)

def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()

# Average of 3 numbers 

def cal_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg

cal_avg(991 , 2838 , 473)

# Default paramerters
def cal_prod(a=2,b=4):
    print(a * b)
    return a*b

cal_prod()

# Practice Question
cities = ["Sailana","Ratlam","Indore","Banglore","Gurgaon"]
heroes = ["Ironman","Thor","Dr.Stranger"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

def print_list(list):
    for item in list:
        print(item, end = " ")

print_list(heroes)
print()

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(7)

def converter(usd_val):
    inr_val = usd_val *83
    print(usd_val, "USD =",inr_val,"INR")

converter(1200)
