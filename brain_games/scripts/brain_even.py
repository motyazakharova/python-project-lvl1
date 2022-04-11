#!/usr/bin/env python3

import random


def main():
    print('Welcome to the Brain Games!')
    NAME = str(input("May I have your name? "))
    print('Hello, {}!'.format(NAME))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = random.randint(1, 100)
        print('Question: ' + str(number))
        answer = input("Your answer: ")
        if number % 2 == 0 and answer == "yes":
            print('Correct!')
        elif number % 2 != 0 and answer == "no":
            print('Correct!')
        else:
          print("It is a wrong answer ;(. Correct your answer.\nLet's try again!'")
          break
    print("Congratulations, {}!".format(NAME))


if __name__ == '__main__':
    main()