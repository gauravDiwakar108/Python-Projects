# Rock, Paper, Scissor

import random
        
        
while True:
    print()
    ask_user = input("********** Are you ready **********\nTo play ROCK, PAPER, SCISSOR ? ").strip().lower()
    if ask_user=='n':
        print("***** Alright catch you next time *****")
        break
    while True:
        c_choice = random.choice(['r', 'p', 's'])
        print()
        user_input = input("Rock(r/R), Paper(p/P), Scissor(s/S) : ").strip().lower()
        
        if user_input not in ['r', 'p', 's']:
            print("Invalid choice. Please enter a valid input (r/p/s).")
            continue
        
        print(f"You choose : {user_input}\nComputer choose : {c_choice}")
        if ((c_choice == 'r') and (user_input == 'p')) or ((c_choice == 'p') and (user_input == 's')) or ((c_choice == 's') and (user_input == 'r')):
            print()
            print("You win!")
            # ask_user = input("Want to play again (Y/N) ? ").strip()
        elif (c_choice == user_input):
            print()
            print("It's a tie!!!")
        else:
            print()
            print("Computer Wins!!!")
        
        ask_user = input("Want to play again (Y/N) ? ").strip().lower()
        
        if ask_user=='n':
            print("***** Thanks for playing *****\n***** Alright catch you next time *****")
            break
        elif ask_user == 'y':
            continue
        else:
            print("Invalid input! Please enter 'y'/'n'")
    if ask_user == 'n':
        break
    
        