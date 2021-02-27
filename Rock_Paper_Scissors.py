
#incorporate random library
import random

# Print Title
print("Let's Play Rock Paper Scissors")

#Specify the three options for the game
options = ("r", "p", "s")

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

#Run Conditionals
winner = "unknown"

if computer_choice == "r":
    if user_choice == "r":
        winner = "tie"
    elif user_choice == "p":
        winner = "user"
    else: # S
        winner = "computer" 
elif computer+choice == "p":
    if user_choice == "r": 
        winner = "computer"
    elif user_choice == "p":
        winner = "tie"
    else: # S
        winner = "user" 
else: #scissors 
    if user_choice == "r": 
        winner = "user"
    elif user_choice == "p":
        winner = "computer"
    else: #s
        winner = "tie"

print(f"user choice is {user_choice}")
print(f"computer choice is {computer_choice}")
print(f"the winner is {winner}")
