# guess the number (user)

import random

def getMinMaxInput():
    min_val = int(input("Enter min value : ").strip())
    max_val = int(input("Enter max value : ").strip())
    
    return min_val, max_val

def getFeedback():
    return input("user, if the guess is correct is high or low or correct (h/l/c) : ").strip().lower()

def computerGuess(guess, min_val, max_val, feedback):
    print(f"Computer guess : {guess}")
    if (feedback == 'h'):
        min_val = guess + 1
        return min_val
    elif (feedback == 'l'):
        max_val = guess - 1
        return max_val
    elif (feedback == 'c'):
        return guess
    else:
        return None
    
def main():
    min_val, max_val = getMinMaxInput()
    feedback = ''
    count = 0
    
    while (feedback != 'c'):
        # print(f"Choose a number b/w {min_val} : {max_val}")
        guess = random.randint(min_val, max_val)
        print(f"Computer guess : {guess}")
        feedback = getFeedback()
        guess = computerGuess(guess, min_val, max_val, feedback)
        count += 1

    print(f"Guess times count : {count}")
        
        
    
# computerGuess(10)

if __name__ == "__main__":
    main()