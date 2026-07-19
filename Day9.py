def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5)

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("END")
show(5)

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(4))

def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx + 1)

fruits = ["mango", "lichi", "guava", "pineapple", "apple"]

print_list(fruits)