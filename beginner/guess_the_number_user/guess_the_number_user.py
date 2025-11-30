# guess the number (user)

import random

def get_min_value():
    return int(input("Enter min value : ").strip())
    

def get_max_value():
    return int(input("Enter max value : ").strip())

def get_feedback():
    return input("user, if the guess is correct is high or low or correct (h/l/c) : ").strip().lower()

def manage_program(guess, feedback):
    if (feedback == 'h'):
        return guess - 1
    elif (feedback == 'l'):
        return guess + 1
    return guess

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
    
    while (feedback != 'c'):
        guess = random.randint(min_val, max_val)
        print(f"\nComputer guess : {guess}")
        feedback = get_feedback()
        count += 1
        if feedback in ['c', 'h', 'l']:
            if feedback == 'h':
                max_val = manage_program(guess, feedback)
                continue
            elif feedback == 'l':
                min_val = manage_program(guess, feedback)
                continue
            result = manage_program(guess, feedback)
            print(f"Correct guess : {result}")
        else:
            print("Please enter h/c/l")
            count = count - 1
            continue
        print(f"Guess times count : {count}")
        break

if __name__ == "__main__":
    main()