# -*- coding: utf-8 -*-
""" This is the mailroom madness script. It will run from the cmd line and
 allow you to generate an email or report based on user input."""

import sys
import math


DONOR_DICT = {'Linus Torvalds': [100, 150, 250],
              'Jane Goodall': [200, 250, 50],
              'Bob Ross': [1000, 550, 1]}


def main_menu_display():
    '''Display user prompt for main menu'''
    user_input = input('''Enter E to send an email,\n
    R for report of donation history\n
    L for a list of all donors,
    or X to exit the program.''')
    user_input = user_input.upper()
    menu_input_validation(user_input)


def menu_input_validation(input):
    '''Validate user input from the main menu'''
    if input != 'X' and input != 'E' and input != 'R' and input != 'L':
        print('\nInvalid input. A valid input is X, E or R.\n')
        main_menu_display()
    else:
        main_menu_input(input)


def main_menu_input(input):
    if input == 'X':
        sys.exit()
    elif input == 'R':
        report()
    elif input == 'E':
        email(input)
    elif input == 'L':
        list_donors(DONOR_DICT)


def report():
    list_build = donor_stat(DONOR_DICT)
    dummy_donor = ['Donor Name', '# of Donations', 'Avg $ Amount', 'Total $ Amount']
    line = '_' * 90
    print(line)
    print('| {:^30} | {:^15} | {:<16} | {:<16} |'.format(dummy_donor[0], dummy_donor[1], dummy_donor[2], dummy_donor[3]))
    print(line)
    for i, donor in enumerate(list_build):
        print('| {:^30} | {:^15} | ${:<15.2f} | ${:<15.2f} |'
              .format(donor[0], donor[2], donor[1], donor[3]))
        print(line)


def donor_stat(DONOR_DICT):
    donor_list = []
    donor_list.clear()
    for name, donation in DONOR_DICT.items():
        don_name = name
        don_total = sum(donation)
        don_num = len(donation)
        don_avg = math.floor(don_total / don_num)
        donor_list.append([don_name, don_total, don_num, don_avg])
    return donor_list


def list_donors(DONOR_DICT):
    '''Returns list of all donors in donor DB stored in DONOR_DICT'''
    print('The list below contains the names of every donor:')
    for name in DONOR_DICT:
        print(name)
    main_menu_display()


def email(input):
    user_input = input('Please enter in a donor name ')
    print(user_input)


def generate_email():
    pass


def add_donor():
    pass


def main():
    """Run the module from the CLI."""
    print('''Welcome to the Mailroom Madness Program.

            Using this module you\'ll be able to display a report of donors and
             their donation history or send a thank you email for their most
              recent donation. You\'ll also be able to display a list of all
               donors names.''')
    main_menu_display()
