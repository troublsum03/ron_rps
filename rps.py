import random

while True:
    choice = input("What is your pick: ")
    choice = choice.lower()

    print("My choice is", choice)

    choices = ['rock', 'paper', 'scissors']

    computer_choice = random.choice(choices)

    print("Computer choice is", computer_choice)
    if choice in choices:
        if choice == computer_choice:
            print('it is a tie')
        if choice == 'rock':
            if computer_choice == 'paper':
                print('you lose, try again :(')
            elif computer_choice == 'scissors':
                print('You win!!! congats :)')
        if choice == 'paper':
            if computer_choice == 'scissors':
                print('you lose, try again :(')
            elif computer_choice == 'rock':
                print('You win!!! congats :)')
        if choice == 'scissors':
            if computer_choice == 'rock':
                print('you lose, try again :(')
            elif computer_choice == 'paper':
                print('You win!!! congats :)')
    else:
        print('invalid choice, try again')

    print()