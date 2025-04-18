import random

num = 0
comChoice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
com = random.choice(comChoice)


def game ():
    num = int(input("Guess a number between 1 and 10:"))
    print (com)
    if (num == com):
        print("You win!")
    else:
        print("aw shucks you got it wrong")

game()