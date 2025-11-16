# Mad Libs is a word-based game where players fill in the blanks in a story with words from different grammatical categories, like nouns, verbs, 
# or adjectives, without seeing the full story first

adj = input("Enter adjective : ").title()
v1 = input("Enter verb 1 : ").title()
v2 = input("Enter verb 2 : ").title()
famous_person = input("Enter a famous person name : ").title()

madlibs = f"Computer progamming is so {adj}! It makes me so excited all the time because I love to {v1}.\
Stay hydrated and {v2} like you are {famous_person}!"

print()
print(madlibs)
                