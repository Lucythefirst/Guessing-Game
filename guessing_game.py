#  Guessing Game
# These programs generate random numbers and you have to guess the number generated

#  This first program will generate a random number, that lies between any two numbers you give it
#  These two numbers are given as arguments in the command line
'''In the terminal, type in this file name, followed by two numbers. These two numbers will provide the range
in which the random number will lie.
e.g file path> guessing_game.py 1 10'''


# import sys
# from random import randint

# num1 = int(sys.argv[1])
# num2 = int(sys.argv[2])
#
# random_num = randint(num1,num2)
#
# def generator():
#     while True:
#         user_guess = int(input("Guess the random no.: "))
#         if user_guess == random_num:
#             print("You guessed right")
#             break
#         else:
#             print("You guessed wrong")
#
# generator()



# OR This program works for a set range:

# from random import randint
# answer = randint(1, 10)
#
# # input from user?
# # check that input is a number 1~10
# while True:
#     try:
#         guess = int(input('guess a number 1~10:  '))
#         if  0 < guess < 11:
#             if guess == answer:
#                 print('you guessed right!')
#                 break
#         else:
#             print('your guess must be between 1 and 10')
#     except ValueError:
#         print('please enter a number')
#         continue

# OR this program is written as functions that can be tested with test.py:

import random


def run_guess(guesss, answer):
    if type(guesss) == int and 0 < guesss < 11:
        if guesss == answer:
            print('you guessed right')
            return True
    else:
        print('the guess must be between 1 and 10')
        return False

if __name__ == '__main__':
    answer = (random.randint(1, 10))
    while True:
        try:
            guesss = int(input('guess a number 1~10:  '))
            if run_guess(guesss, answer):
                break
        except ValueError:
            print('please enter a number')
            continue

