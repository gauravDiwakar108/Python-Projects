# guess the number (user)

import random

def get_min_value():
    return int(input("Enter min value : ").strip())
    

def get_max_value():
    return int(input("Enter max value : ").strip())

def get_feedback():
    return input("user, if the guess is correct is high or low or correct (h/l/c) : ").strip().lower()

def computerGuess(guess, min_val, max_val, feedback):
    # print(f"Computer guess : {guess}")
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

def get_valid_input(prompt_func):
    while True:
        try:
            return prompt_func()
        except ValueError as ve:
            print(f"Invalid Input : {ve}\n")
def main():
    min_val = get_valid_input(get_min_value)
    max_val = get_valid_input(get_max_value)
    feedback = ''
    count = 0
    
    while (feedback != 'c' and min_val != max_val):
        # print(f"Choose a number b/w {min_val} : {max_val}")
        guess = random.randint(min_val, max_val)
        print(f"\nComputer guess : {guess}")
        feedback = get_feedback()
        if feedback in ['h', 'l', 'c']:
            guess = computerGuess(guess, min_val, max_val, feedback)
        count += 1

    print(f"Guess times count : {count}")
        
        
    
# computerGuess(10)

if __name__ == "__main__":
    main()