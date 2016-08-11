# -*- coding: utf-8 -*-

""" This is the mailroom madness script. It will run from the cmd line and allow you to generate an email or report based on user input"""


DONOR_DICT = {{'John Doe': [100, 150, 250]}, {'Jane Doe': [200, 250, 50]}, {'Bob Ross': [1000, 550, 1]}}


def main_menu():
    print('Welcome to the Mailroom Script. Using this script you\'ll be able to display a report of donors and their cumulative donation totals or send a thank you email based on the most recent donation.')
    user_input = input('Enter E for email, R for report or X to exit the script')
