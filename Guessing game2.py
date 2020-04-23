import random
from typing import Any, Union

var1 = random.randint(1, 25)
Gender = input("Enter your Gender: M or F \t").upper()
running = False

while Gender != "M" and Gender != "F":
    Gender = input("Enter the correct gender \t").upper()
    if Gender == "M" or Gender == "F":
        break

if Gender == "M" or Gender == "F":
    running = True
print("Guess a number between 1 to 25 \n")
while running:
    number = int(input())
    if number > var1:
        print('Try to guess lower')
    elif number < var1:
        print('Try to guess higher')
    else:
        if number == var1 and Gender == "M":
            print('CONGRATULATIONS, KING! YOU HAVE GUESSED THE CORRECT NUMBER')
        elif number == var1 and Gender == "F":
            print('CONGRATULATIONS, QUEEN! YOU HAVE GUESSED THE CORRECT NUMBER')
        break
