# Mad Libs is a word-based game where players fill in the blanks in a story with words from different grammatical categories, like nouns, verbs, 
# or adjectives, without seeing the full story first

def getUserInput():
    """getting user input"""
    
    adj = input("Enter adjective : ").strip().title()
    verb1 = input("Enter verb 1 : ").strip().title()
    verb2 = input("Enter verb 2 : ").strip().title()
    famous_person = input("Enter a famous person name : ").strip().title()
    
    return adj, verb1, verb2, famous_person

def madlib(adjective, verb1, verb2, famous_person):
    """
    Returns: 
    str: A formatted madlib string.
    """
    
    return f"""Computer progamming is so {adjective}!
It makes me so excited all the time because I love to {verb1}.
Stay hydrated and {verb2} like you are {famous_person}!""".strip()

def checkIfAlphabet(*args):
    return all(word.replace(" ", "").isalpha() for word in args)


def main():
    while True:
        try:
            adjective, verb1, verb2, famous_person = getUserInput()
            if checkIfAlphabet(adjective, verb1, verb2, famous_person):
                print()
                result = madlib(adjective, verb1, verb2, famous_person)
                print(result)
                ask_user = input("Do you want to play again (y/n)? ").strip().lower()
                if ask_user=='y':
                    continue
                break
            else:
                raise ValueError("Please enter alphabets only not other type of value")
        except ValueError as ve:
            print()
            print(ve)
    
if __name__ == "__main__":
    main()
