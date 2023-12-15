import random

def start_message():
    print('Start rock-paper-scissors\\''')


def get_player():
    print('Input your hand')
    return int(input('0:rock, 1:scissors, 2:paper'))

def get_computer(): 
    return random.randint(0, 2)


def view_result(hand_diff):
    if hand_diff == 0:
        print('draw')
    elif hand_diff == -1 or hand_diff == 2:
        print('win')
    else:
        print('lose')

start_message()

your_hand = get_player()
computer_hand = get_computer()
hand_diff = your_hand - computer_hand

view_result(hand_diff)