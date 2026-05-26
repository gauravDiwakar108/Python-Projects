print("Welcome to my computer quize!")

playing = input("Do you want to play? ('Yes', 'No') ").lower()

if playing != 'yes':
    print("Okay! see you next time.")
    quit()

print("Okay! Let's play :)")

score = 0

# question 1
answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")

# question 2
answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")

# question 3
answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")

# question 4
answer = input("What does ROM stand for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")

# question 5
answer = input("What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
    
total = 10
print(f"You've got {score} marks out of {total}")