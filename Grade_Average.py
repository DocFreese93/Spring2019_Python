# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 20:27:20 2019

@author: Milo
"""

# Declare variables and obtain user input
score_1 = float(input('Enter first score: '))
score_2 = float(input('Enter second score: '))
score_3 = float(input('Enter third score: '))

# Determine average of 3 grades
average = round(((score_1 + score_2 + score_3) / 3), 2)

# Display Average
print('\nAverage of 3 scores: ', average)