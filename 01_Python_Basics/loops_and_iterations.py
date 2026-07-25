#CH - 5 (Loops)

# "While" Loop
i = 1
while i <= 100:   #Stopping Condition
    print("Damru", i)
    i += 1

#Question Practice
i = 1
while i <= 5:
    print(i)
    i += 1

i = 1
while i<=100:
    print(i)
    i += 1

i = 100
while i >= 1:
    print(i)
    i -= 1

i = 1
while i <= 10:
    print(3*i)
    i += 1

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while  idx < len(nums):
    print(nums[idx])
    idx += 1

# break word in While Loop
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break    # Stop
    i += 1

print("end of loop")

# continue in While Loop
i = 0
while i <= 5:
    if(i == 3):
        continue   # Skip 
    print(i)
    i += 1

