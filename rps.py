from mymod import get_string
import random
from time import sleep

def choose(str):
    a = get_string(str)
    b = 0

    while True:

        if a == 'rock' or a == 'paper' or a == 'scissors':
            return a
        else:
            a = get_string(str)

def pw():
    print("Player wins!" + "\n" * 6)

def cw():
    print("Computer wins!" + "\n" * 6)


choices = ['rock', 'paper', 'scissors']

computer_points = 0
player_points = 0



while True:
    #display points
    print('\n' + 'Computer: ' + str(computer_points))
    print('Player: ' + str(player_points) + '\n')

    #choices
    player_choice = choose("Play: ")

    pc = 0
    cc = 0

    for x in range(3):
            if player_choice == choices[x]:
                pc += x
                break

    computer_choice = random.choice(choices)

    for y in range(3):
            if computer_choice == choices[y]:
                cc += y
                break

    sleep(1)

    print("computer's play: " + computer_choice)

    sleep(1)

    #check for tye
    if (cc == pc):
        print("Tye")
    elif (cc == 0 and pc == 1):
        player_points += 1
        pw()

    elif (cc == 0 and pc == 2):
        computer_points += 1
        cw()

    elif (cc == 1 and pc == 0):
        computer_points += 1
        cw()

    elif (cc == 1 and pc == 2):
        player_points += 1
        pw()

    elif (cc == 2 and pc == 0):
        player_points += 1
        pw()

    elif (cc == 2 and pc == 1):
        computer_points += 1
        cw()


    