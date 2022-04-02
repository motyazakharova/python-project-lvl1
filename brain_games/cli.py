#!/usr/bin/env python3

import prompt


def welcome_user():
    NAME = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(NAME))
    