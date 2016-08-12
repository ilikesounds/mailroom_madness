# -*- coding: utf-8 -*-
""" This is the mailroom madness script. It will run from the cmd line and
 allow you to generate an email or report based on user input."""

import sys
import math
import pprint


DONOR_DICT = {'Linus Torvalds': [100, 150, 250],
              'Jane Goodall': [200, 250, 50],
              'Bob Ross': [1000, 550, 1]}


def main_menu_display():
    user_input = input('Enter E to send an email,\nR for report of donation history\nor X to exit the program.\n')
    user_input = user_input.upper()
    validation(user_input)


def validation(input):
    if input != 'X' and input != 'E' and input != 'R':
        print('\nInvalid input. A valid input is X, E or R.\n')
        main_menu_display()
    else:
        main_menu_input(input)


def main_menu_input(input):
    if input == 'X':
        sys.exit(0)
    elif input == 'R':
        report(input)
    elif input == 'E':
        email(input)


def report():
    list_build = donor_stat(DONOR_DICT)
    for i, donor in enumerate(list_build):
        print('Donor {} has donated {} times. Of those donations, the avg donation is {}. The total amount of donations is {}'.format(donor[0], donor[2], donor[1], donor[3]))


def donor_stat(DONOR_DICT):
    donor_list = []
    donor_list.clear()
    for name, donation in DONOR_DICT.items():
        don_name = name
        print(don_name)
        don_total = sum(donation)
        don_num = len(donation)
        don_avg = don_total / don_num
        donor_list.append([don_name, don_total, don_num, don_avg])
    return donor_list


def email(input):
    pass


def main():
    """Run the module from the CLI."""
    print('Welcome to the Mailroom Madness Program.\n\nUsing this module you\'ll be able to display a report of donors\nand their donation history or send a thank you email for their\nmost recent donation.\n')
    main_menu_display()
