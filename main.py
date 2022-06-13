# Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules. You can find the official rules under the Resources.
import random

options = ["R","P","S"]
print('Welcome to the Rock-Paper-Scissors game')
print('-'*100) 
print("To start pick: \n 'R' for 'rock'\n 'P' for 'paper',\n 'S' for 'scissors'")
print('-'*100)

while True:
    cpu_choice = random.choice(options)
    player_choice = input('Your pick here: ').upper()

    if player_choice in options:
        print('Player ({}) : CPU ({})'.format(player_choice,cpu_choice))
        
        if player_choice != cpu_choice:
            print('Your choice is wrong. Pick again')

        else:
            print('You won, Bravo !!')
            exit()

    else:
        print("Invalid option, pick rightly")

