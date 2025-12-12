import random

def manage_program(guess, feedback):
    if (feedback == 'h'):
        return guess - 1
    elif (feedback == 'l'):
        return guess + 1
    return guess

min_val = 1
max_val = 10

ask_user = ''
while ask_user != 'c':
    c_guess = random.randint(min_val, max_val)
    print(f"Computer guess : {c_guess}")
    ask_user = input("Is this correct guess : ").strip().lower()
    
    if ask_user in ['c', 'h', 'l']:
        if ask_user == 'h':
            max_val = manage_program(c_guess, ask_user)
            continue
        elif ask_user == 'l':
            min_val = manage_program(c_guess, ask_user)
            continue
        result = manage_program(c_guess, ask_user)
        break
        
    
    # if ask_user == 'c':
    #     break
    # elif ask_user == 'h':
    #     max_val = c_guess - 1
    #     continue
    # elif ask_user == 'l':
    #     min_val = c_guess + 1
    #     continue
    # else:
    #     print("Please enter h/c/l")
    
    
        
    