# -*- coding: utf-8 -*-
""" This is the mailroom madness script. It will run from the cmd line and allow you to generate an email or report based on user input"""


from sys import exit, argv


DONOR_DICT = {'John Doe': [100, 150, 250],
              'Jane Doe': [200, 250, 50],
              'Bob Ross': [1000, 550, 1]}


def main_menu_display():
    print('Welcome to the Mailroom Script. Using this script you\'ll be able to display a report of donors and their cumulative donation totals or send a thank you email based on the most recent donation.')
    user_input = input('Enter E for email, R for report or X to exit the script')
    user_input = user_input.lower()
    validation(user_input)


def validation(user_input):
    if user_input != 'X' or user_input != 'E' or user_input != 'R':
        print('You have not entered a valid input.')
        main_menu_display()
    else:
        main_menu_input()


def main_menu_input(user_input):
    if user_input == 'X':
        sys.exit(0)
    elif user_input == 'R':
        report()
    elif user_input == 'E':
        email()


def report():
    pass


def email():
    pass
