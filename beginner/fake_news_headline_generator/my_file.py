from random import choice

subjects = ['akshay kumar', 'pretti zenta', 'kabir', 'modi', 'kejriwal']
actions = ['dancing', 'washing clothes', 'crying', 'walking', 'standing']
places = ['delhi', 'mumbai', 'gali number 16', 'kirana store', 'mall', 'yamuna']

while True:
    pick_subject = choice(subjects)
    pick_action = choice(actions)
    pick_place = choice(places)

    headline = f"{pick_subject} is {pick_action} at {pick_place}"
    print(headline)
    
    ask_user = input("Do you want to play again? ").strip().lower()
    if ask_user in ['y', 'n']:
        if ask_user == 'n':
            break