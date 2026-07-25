# CH - 7 (File I/O)
f  = open("Day6.py" ,"r")
data = f.read()
print(data)
print(type(data))
f.close()

# Character             Meaning

#    'r'       -        open for reading(default)
#.   'w'       -        open for writing,truncating the file first
#.   'x'       -        create a new file and open it for writing
#.   'a'       -        open for writing, appending to the end of the file if it exists
#.   'b'       -        binary mode
#.   't'       -        text mode(default)
#.   '+'       -        open a disk file for updating(reading and writing)

# Reading in file
f = open("Day6.py","r")
data = f.read(6)
print(data)
f.close()

f = open("Day6.py","r")
data = f.readline()
print(data)
f.close()

f = open("Day6.py","r")
data = f.read()
print(data)
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()



