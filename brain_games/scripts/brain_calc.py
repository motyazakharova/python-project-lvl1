#!/usr/bin/env python3

import operator
import random


def main():
    print('Welcome to the Brain Games!')
    NAME = str(input("May I have your name? "))
    print('Hello, {}!'.format(NAME))
    print('What is the result of the expression?')
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    success = False
    for i in range(3):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        oper, result = random.choice(operators)
        prompt = "Question: {} {} {}\nYour answer: ".format(num1, oper, num2)
        reply = int(input(prompt))
        if reply == result(num1, num2):
            print('Correct!')
            success = True
        else:
            print("{} is wrong answer ;(. Correct answer was {}.\nLet's try again, {}!".format(reply, result(num1, num2), NAME))
            success = False
            break
    if success:
        print("Congratulations, {}!".format(NAME))


if __name__ == '__main__':
    main()
