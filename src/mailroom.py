# -*- coding: utf-8 -*-
""" This is the mailroom madness script. It will run from the cmd line and
 allow you to generate an email or report based on user input."""

import sys
import math


DONOR_DICT = {'John Doe': [100, 150, 250],
              'Jane Doe': [200, 250, 50],
              'Bob Ross': [1000, 550, 1]}


def main_menu_display():
    print('Welcome to the Mailroom Madness Program.\n\nUsing this module you\'ll be able to display a report of donors\nand their donation history or send a thank you email based\nfor their most recent donation.\n')
    user_input = input('Enter E to send an email,\nR for report of donation history\nor X to exit the program.\n')
    user_input = user_input.upper()
    validation(user_input)


def validation(input):
    if input != 'X' or input != 'E' or input != 'R':
        print('A valid input is X, E or R. You have not entered a valid input.')
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


def report(DONOR_DICT):
    donor_list = list(DONOR_DICT.keys())
    for idx in donor_list:
        don_name = idx
        don_total = sum(DONOR_DICT[idx])
        don_num = len(DONOR_DICT[idx])
        don_avg = don_total / don_num
        math.floor(don_avg)
    return don_name, don_num, don_avg, don_total


def email():
    pass


def main():
    """Run the module from the CLI."""
    main_menu_display()
