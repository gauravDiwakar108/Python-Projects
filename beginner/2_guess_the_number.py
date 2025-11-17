# Guess the number (Computer)

import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    
    while guess != random_num:
        guess = int(input(f"Guess a number b/w 1 and {x} : ").strip())
        
        if (guess < random_num):
            print()
            print("Too low. Guess again!.")
        elif (guess > random_num):
            print()
            print("Too High. Guess again!")
    print()
    print(f"Correct guess!!!")
    print(random_num)
        
guess(10)