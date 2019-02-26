# -*- coding: utf-8 -*-
"""
Milo Freese
2/20/19
Python 1 - DAT-119 - Spring 2019
Homework 3

Write a tip calculator. Have the user enter the price of the bill, and 
your program should tell them their total for a 10%, 15%, and 20% tip

"""

# Declare variables and obtain user input
bill_price = float(input('Enter the bill price: '))

ten_percent_tip_amount = (bill_price * .1) + bill_price
fifteen_percent_tip_amount = bill_price * .15 + bill_price
twenty_percent_tip_amount = bill_price * .2 + bill_price

# Display bill total for tip percentages
print('$', ten_percent_tip_amount)
print('$', fifteen_percent_tip_amount)
print('$', twenty_percent_tip_amount)