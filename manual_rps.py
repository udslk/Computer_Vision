import random

def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def get_user_choice():
    while True:
        letter = input('Enter your choice by typing R for Rock, P for Paper and S for Scissors:')
        if letter.lower() == 'r':
            return 'Rock'
            break
        elif letter.lower() == 'p':
            return 'Paper'
            break
        elif letter.lower() == 's':
            return 'Scissors'
            break
        else:
            print('It is an incorrect choice') 

def get_winner(computer_choice, user_choice):
    
    if [computer_choice,user_choice] in [['Rock','Scissors'],['Paper','Rock'],['Scissors','Paper']]:
        winner = 'Computer'
    elif [user_choice,computer_choice] in [['Rock','Scissors'],['Paper','Rock'],['Scissors','Paper']]:
        winner = 'User'
    else:
        winner = 'No One'
    return winner

def play():
    computor_choice =  get_computer_choice()
    user_choice = get_user_choice()

    winner = get_winner(computor_choice, user_choice)
    if winner == 'User':
        print('You win the game, CONGRATULATIONS')
    elif winner == 'Computer':
        print('Computer wins the game')
    else:
        print('No one Wins the game')

#if __name__ == '__main__':
play()


