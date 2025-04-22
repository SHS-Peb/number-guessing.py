import random

num = 0
comChoice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
com = random.choice(comChoice)


def game ():
    guess = None
    num = int(input("Guess a number between 1 and 10:"))
    com = random.choice(comChoice)
    while num != com:
        num = int(input("Guess a number between 1 and 10:"))
        if num == com:
            print(f'I was thinking of {com}! You Win!')
        else:
            print(f'Aw shucks no. Try again?')

game()