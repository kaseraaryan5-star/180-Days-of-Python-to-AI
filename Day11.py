# Writiing in file
f = open("sample.txt", "w")
f.write("My name is Yashasvi Kasera")
f.close()

f = open("sample.txt","a")
f.write("\nI am studying in college")
f.close()

f = open("sample.txt","r+")
f.write("DAMRU")
f.close()

f = open("sample.txt", "r+")
f.write("Damru")
print()
f.close()

f = open("sample.txt","w+")
print(f.read())
f.write("abc")
f.close()

f = open("sample.txt","a+")
print(f.read())
f.write("abc")
f.close()

with open("sample.txt", "r") as f: 
    data = f.read()
    print(data)

with open("sample.txt", "w") as f:
    f.write("new data")

import os
os.remove("demo.txt")

