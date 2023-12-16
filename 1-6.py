import random

hands = ['rock', 'scissors', 'paper']

def start_message():
    print('Start \'rock-paper-scissors')

def get_player():
    print('Input your hand')
    input_message = ''
    index = 0
    for hand in hands:
        input_message += str(index) + ':' +hand
        if index < 2:
            input_message += ', '
        index += 1
    return int(input(input_message))

def get_computer():
    return random.randint(0, 2)

def get_hand_name(hand_number):
    return hands[hand_number]

def view_hand(your_hand, computer_hand):
    print('My hand is' + get_hand_name(your_hand))  
    print('Rival\' is' + get_hand_name(computer_hand))         

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

view_hand(your_hand, computer_hand)
view_result(hand_diff)