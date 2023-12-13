mport random

print('Start rock-paper-scissors game')

print('Input your hand choice')
my_hand = int(input('0: rock, 1: scissors, 2: papers'))
computer_hand = random.randint(0, 2)

if my_hand == 0:
    if computer_hand == 0:
        print('Draw')
    elif computer_hand == 1:
        print('Win')
    else:
        print('Lose')
elif my_hand == 1:
    if computer_hand == 0:
        print('Lose')
    elif computer_hand == 1:
        print('Draw')
    else:
        print('Win')
elif my_hand == 2:
    if computer_hand == 0:
        print('Win')
    elif computer_hand == 1:
        print('Lose')
    else:
        print('Draw')
else:
    print('Invalid input. Please enter 0, 1, or 2 for rock, scissors, or papers respectively.')
