# Mad Libs is a word-based game where players fill in the blanks in a story with words from different grammatical categories, like nouns, verbs, 
# or adjectives, without seeing the full story first

def getUserInput():
    """getting user input"""
    
    adj = input("Enter adjective : ").title()
    verb1 = input("Enter verb 1 : ").title()
    verb2 = input("Enter verb 2 : ").title()
    famous_person = input("Enter a famous person name : ").title()
    
    return adj, verb1, verb2, famous_person

def madlib(adjective, verb1, verb2, famous_person):
    """
    Generate a madlib-style sentence using the provided inputs.
    
    Parameters:
    adjective (str): An adjective to describe programming.
    verb1 (str): A verb describing an action.
    verb2 (str): A verb describing another action.
    famous_person (str): The name of a famous person to include.
    
    Returns:
    str: A formatted madlib string.
    """
    
    return f"""Computer progamming is so {adjective}!
It makes me so excited all the time because I love to {verb1}.
Stay hydrated and {verb2} like you are {famous_person}!""".strip()


def main():
    adjective, verb1, verb2, famous_person = getUserInput()
    print()
    result = madlib(adjective, verb1, verb2, famous_person)
    
    print(result)
    
if __name__ == "__main__":
    main()
    

                