import random

hands = ['rock', 'scissors', 'paper']

def start_message():
    print('start \'rock-paper-scissors\'')

def get_player():
    print('Input your hand')
    return int(input('0:rock, 1:scissors, 2:paper'))

def get_computer():
    return random.randint(0,2) 

def get_hand_name(hand_number):
    return[hand_number]

def view_hand(your_hand, computer_hand):
    print()   