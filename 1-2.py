import random

print('Start rock-paper-scissors')

print('Input your hand')
your_hand = int(input('0: rock, 1: scissors, 2: paper'))
computer_hand = random.randint(0, 2)

if your_hand == 0:
    if computer_hand == 0:
        print('Draw')
    elif computer_hand == 1:
        print('Win')
    elif computer_hand == 2:
        print('Lose')
elif your_hand == 1:
    if computer_hand == 0:
        print('Lose')
    elif computer_hand == 1:
        print('Draw')
    elif computer_hand == 2:
        print('Win')
elif your_hand == 2:
    if computer_hand == 0:
        print('Win')
    elif computer_hand == 1:
        print('Lose')
    elif computer_hand == 2:
        print('Draw')
else:
    print('Invalid input. Please enter 0, 1, or 2 for rock, scissors, or paper respectively.')