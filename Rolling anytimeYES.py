import random

print("The random number is:")

for x in range(1):
    print(random.randint(1, 6))

while True:
    answer = input("Do you want to roll again? 'yes' or 'no' : ")

    if answer.lower() in ['y','yes', 'of course']:
        print('Yes')
        for x in range(1):
            print("The new number is:")
            print(random.randint(1, 6))


    elif answer.lower() in ['n', 'no', 'never']:
        print('No')
        print("Thanks for playing.")
        break

    else:
        print("Wrong answer.")
        break