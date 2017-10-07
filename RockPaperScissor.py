from random import randint

player = input('rock(r), paper(p) or scissors(s)?')
print(player, 'vs', end=' ')

chosen = randint(1, 3)
# print (chosen)

if chosen == 1:
    computer = 'r'

elif chosen == 2:
    computer = 'p'

elif chosen == 3:
    computer = 's'

else:
    print("Wrong input")

print(computer)

if player == computer:
    print('DRAW')

elif player == 'r' and computer == 's':
    print('YOU WON')

elif player == 's' and computer == 'r':
    print('YOU LOOSE')

elif player == 'p' and computer == 'r':
    print('YOU WON')

elif  player == 'p' and computer =='s':
    print('YOU LOOSE')