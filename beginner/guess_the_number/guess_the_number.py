# Guess the number (Computer)

import random

def get_min_value():
    return int(input("Enter min value : ").strip())

def get_max_value():
    return int(input("Enter max value : ").strip())

def random_num(x, y):
    # set guess number
    rand_num = random.randint(x, y)
    return rand_num

def get_user_guess(x, y):
    # getting user guess
    return int(input(f"Guess a number b/w {x} and {y} : ").strip())


def guess(x, y):
    if (x > y):
        return "Too low. Guess again!"
    elif (x < y):
        return "Too High. Guess again!"
    return "\nCorrect Guess!!!"


def get_valid_input(prompt_func):
    while True:
        try:
            return prompt_func()
        except ValueError as ve:
            print(f"Invalid input : {ve}\n")

def main():
    min_val = get_valid_input(get_min_value)
    max_val = get_valid_input(get_max_value)
    
    rand_num = random_num(min_val, max_val)
    user_guess = 0
    guess_count = 0
    
    while user_guess != rand_num:
        print()
        user_guess = get_valid_input(lambda : get_user_guess(min_val, max_val))
        result = guess(rand_num, user_guess)
        guess_count += 1
        print(result)
    print(f"User guessed the nubmer in {guess_count} guess.")
    
if __name__ == "__main__":
    main()