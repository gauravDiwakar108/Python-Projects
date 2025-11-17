# guess the number (user)

import random

def computerGuess(x):
    low = 1
    high = x
    
    feedback = ''
    count = 0
    while (feedback != 'c') and (low != high):
        guess = random.randint(low, high)
        count += 1
        print(guess)
        feedback = input("user, if the guess is correct is high or low or correct (h/l/c) : ").strip().lower()
        if (feedback == 'l'):
            low = guess + 1
        elif (feedback == 'h'):
            high = guess - 1
    
    print()
    print("correct guess")
    
    print(f"Guess times count : {count}")
    
computerGuess(10)