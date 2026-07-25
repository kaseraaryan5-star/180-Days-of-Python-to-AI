# # Guess Number

import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit :")
    if(userChoice == "Quit"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess !!")
        break
    elif(userChoice < target):
        print("your number was too small. Take a bigger guess...")
    else:
        print("your number was too big. Take a small guess...")

print("-----GAME OVER-----")

# Random Password Generator

import random
import string

pass_len = 8
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("your random password is :", password)