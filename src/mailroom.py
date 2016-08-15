# -*- coding: utf-8 -*-
""" This is the mailroom madness script. It will run from the cmd line and
 allow you to generate an email or report based on user input."""

import os
import sys
import math


DONOR_DICT = {'Linus Torvalds': [100, 150, 250],
              'Jane Goodall': [200, 250, 50],
              'Bob Ross': [1000, 550, 1]}


def main_menu_input():
    '''Display user prompt for main menu'''
    user_input = input('''
    Main Menu:
    E to generate a thank you email to send to a donor
    R for a report on the donation history of all donors
    Type exit at any prompt to exit the program.

    >>>''').upper()
    menu_input_validation(user_input)


def email_donor_input():
    user_input = input('''
    Please enter in a donor name.
    Type list for a list of all donors.
    Type menu to return to the main menu prompt.

    >>>''').upper()
    email_input_validation(user_input)


def email_donation_input():
    user_input = int(input('''
    Please enter the donation amount in numbers only.
    >>>'''))
    if type(user_input) == int or type(user_input) == float:
        return float(user_input)
    else:
        email_donation_input()


def menu_input_validation(user_input):
    '''Validate user input from the main menu'''
    if user_input != 'EXIT' and user_input != 'E' and user_input != 'R':
        print('\nInvalid input. A valid input is X, E or R.\n')
        main_menu_input()
    else:
        main_menu_route(user_input)


def email_input_validation(user_input):
    '''Validate user input from the email menu'''
    if user_input == 'LIST':
        list_donors(DONOR_DICT)
    elif user_input == 'MENU':
        main_menu_input()
    elif user_input == 'EXIT':
        sys.exit(0)
    else:
        donor_db_check(user_input)


def main_menu_route(user_input):
    if user_input == 'X':
        sys.exit()
    elif user_input == 'R':
        report()
    elif user_input == 'E':
        email_donor_input()


def report():
    '''Displays donor stats report'''
    os.system('clear')
    list_build = donor_stat(DONOR_DICT)
    dummy_donor = ['Donor Name', '# of Donations', 'Avg $ Amount',
                   'Total $ Amount']
    print('-' * 90)
    print('| {:^30} | {:^15} | {:<16} | {:<16} |'.format(dummy_donor[0],
          dummy_donor[1], dummy_donor[2], dummy_donor[3]))
    for i, donor in enumerate(list_build):
        print('| {:^30} | {:^15} | ${:<15.2f} | ${:<15.2f} |'
              .format(donor[0], donor[2], donor[1], donor[3]))
    main_menu_input()


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
    os.system('clear')
    print('The list below contains the names of every donor:\n')
    for name in DONOR_DICT:
        print(name)
    print('\n' * 2)
    email_donor_input()


def email(user_input):
    '''Generates a thank-you email to send to donors'''
    email_donor_input()


def generate_email(donor, donate_amt):
    '''Takes the name from db check and generates email for the user'''
    print('''
    Dear {},

    Thank you for your kind donation of ${:.2f}.
    We at the Puget Sound Paunch Preservation Society appreciate your support!
    Your donation will keep us awash in our favorite cardinal sins.
    Gluttony. And Sloth.

    Best,

    PSPPS
    '''.format(donor.title(), donate_amt))
    email_donor_input()


def add_donor(donor):
    donate_amt = email_donation_input()
    print(type(donate_amt))
    DONOR_DICT.setdefault(donor, []).append(int(donate_amt))
    generate_email(donor, donate_amt)


def donor_db_check(user_input):
    donor = user_input.title()
    if donor in DONOR_DICT:
        donate_amt = email_donation_input()
        DONOR_DICT[donor].append(donate_amt)
        generate_email(user_input, donate_amt)
    else:
        print('That donor doesn\'t exist in our DB. We\'ll add them now.')
        add_donor(donor)


def main():
    """Run the module from the CLI."""
    os.system('clear')
    print('''
    Welcome to the Mailroom Madness Program.

    Using this module you\'ll be able to:
    1. Display a report of donors and their donation history.
    2. Send a thank you email to a donor for their most recent donation.
    3. You\'ll also be able to display a list of all donors names.
    ''')
    main_menu_input()


if __name__ == '__main__':
    main()
