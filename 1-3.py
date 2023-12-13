import random

print('Start rock-paper-scissors ')
print('Input your hand')
your_hand = int(input('0: rock, 1: scissors, 2: paper'))
computer_hand = random.randint(0, 2)

hand_diff = your_hand - computer_hand

if hand_diff == 0:
    print('Draw')
elif hand_diff == -1 or hand_diff == 2:
    print('Win')
else:
    print('Lose')