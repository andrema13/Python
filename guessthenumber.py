import random

number = (random.randint(0, 100))


while True:
    answer = int(input("I guess number: "))

    if answer and number < answer:
        print("Too much!")

    elif answer and number > answer:
        print("Want more!")

    else:
        print("Nice work, you won!")
        break




