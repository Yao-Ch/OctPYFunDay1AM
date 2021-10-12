"""
Exercise 3: (ExercisePy1.pdf)

1) Generate a secret random integral number ([1,100]) (see the module random)
2) With the help of a loop:
    a) prompt the user for an integral number
    b) increment a variable that count the current number of attempts to guess
    the secret number
    c) compare the number entered with the secret number
    d) print an appropriate message: "Too small", "Too large", "Bingo!!"
    e) if the secret number is found: leave the loop and stop the script
    
    You should also leave the loop after 6 attempts to guess the secret number
3) If, at the end of the loop, the secret number is not found print a message 
    with the value of the secret number
"""

import random

secret=random.randint(1,100)

print(secret)

currentNumberOfAttempts=0
currentValue=0

while secret != currentValue and currentNumberOfAttempts < 6:
    currentValue=input(f"Enter an int in the range [1,100] ({currentNumberOfAttempts+1}/6): ")
    currentValue=int(currentValue)
    if currentValue == secret:
        print ("Bingo ! You've found the secret number")
    elif currentValue > secret:
        print("Too large !")
    elif currentValue < secret:
        print("Too small")
    # currentNumberOfAttempts = currentNumberOfAttempts + 1
    currentNumberOfAttempts += 1
    
if secret != currentValue:
    print("The secret number was:", secret)
    
    
    
    