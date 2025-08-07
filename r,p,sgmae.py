#ROCK, PAPER, SCISSOR GMAE!!!

import random

while True:
    choices = ("r", "p", "s")
    user_choice=input("Rock, Paper, or Scissors? (R/P/S):" ) .lower()
    
    if user_choice not in choices:
        print("invalid input!")
        continue
    
    computer_choice= random.choice(choices)
    
    full_choices= {"r": "Rock", "p": "Paper", "s": "Scissor"}
    print(f"you chose {full_choices [user_choice]}")
    print(f"computer chose {full_choices [computer_choice]}")

    if user_choice == computer_choice :
        print("Tie!")
    elif\
    (user_choice=="r" and computer_choice=="s") or \
    (user_choice=="p" and computer_choice=="r") or \
    (user_choice=="s" and computer_choice=="p"): 
        print("You win!!")
    
    else:  
        print("You lose!!")

    should_continue= input("continue? (y/n)").lower()
    if should_continue=="n":
        print("Thanks for playing!!")
        break
