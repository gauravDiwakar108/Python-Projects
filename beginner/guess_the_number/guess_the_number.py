# Guess the number (Computer)

import random

def getMinValue():
    return int(input("Enter min value : ").strip())

def getMaxValue():
    return int(input("Enter max value : ").strip())

def randomNum(x, y):
    # set guess number
    rand_num = random.randint(x, y)
    return rand_num

def getUserGuess(x, y):
    # getting user guess
    return int(input(f"Guess a number b/w {x} and {y} : ").strip())


def guess(x, y):
    # while guess != random_num
    
    if (x > y):
        return "Too low. Guess again!"
    elif (x < y):
        return "Too High. Guess again!"
    return "Correct Guess!!!"

def main():
    min_val = getMinValue()
    max_val = getMaxValue()
    random_num = randomNum(min_val, max_val)
    
    user_guess = 0
    
    while user_guess != random_num:
        user_guess = getUserGuess(min_val, max_val)
        result = guess(random_num, user_guess)
        print(result)
    
if __name__ == "__main__":
    main()