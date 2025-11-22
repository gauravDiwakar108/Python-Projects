import random
from words import words
import string

def getValidWord(words):
    word = random.choice(words) # randomly chooses a word from words list
    while ('-' in word) or (' ' in word):
        word = random.choice(words)
    return word.upper()

def hangman():
    word = getValidWord(words)
    word_letters = set(word) # all letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what user has guessed
    
    lives = 6
    
    # getting user input
    while len(word_letters)>0 and lives > 0:
        print(f"You've {lives} lives and you've already used these letters: {' '.join(used_letters)}")
        
        # what the current word is (i.e W-RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f"Current word : {' '.join(word_list)}")
        
        user_letter = input("\nGuess a letter : ").strip().upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else:
                lives -= 1 # takes away one live if wrong
                print("Letter is not in the word.")
        
        elif user_letter in used_letters:
            print("You've already used that character. Please try another letter")
        else:
            print("Invalid character. Please try again!")
    
    if lives == 0:
        print(f"You died, sorry. The word was : {word}")
    else:
        print(f"You've guessed the word correctly: {word}!!!")
            
    
    
    
# user_input = input("Type something : ")
# print(user_input)

# print(words)

hangman()