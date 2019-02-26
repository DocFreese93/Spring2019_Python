# -*- coding: utf-8 -*-
"""
Milo Freese
2/20/19
Python 1 - DAT-119 - Spring 2019
Homework 3

Write a program that asks the user for three grades, averages them, and outputs the average grade. 
"""

# Declare variables and obtain user input
score_1 = float(input('Enter first score: '))
score_2 = float(input('Enter second score: '))
score_3 = float(input('Enter third score: '))

# Determine average of 3 grades
average = round(((score_1 + score_2 + score_3) / 3), 2)

# Display Average
print('\nAverage of 3 scores: ', average)
