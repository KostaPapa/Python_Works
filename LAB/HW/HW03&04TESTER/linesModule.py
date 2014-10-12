#!C:\Users\kpapa01\Desktop\Python\hw\hw03\linesModule.exe

''' 
cs1114 

Submission: hw03
Required Filename: linesModule.py

Programmer: Kostaq Papa
Username: kpapa01
ID Number : 0412768

Purpose of program: The purpose of this program is to make module of line drawing functions.

'''

MIN_RANDOM_VALUE = 8    # The minimum random value that a length of charcters will have.
MAX_RANDOM_VALUE = 17   # The maximum random value that a length of characters will have.


import random


def drawTwoCharLine (charOne, charTwo, lengthOfLine, nextLine = True):
    '''This function will draw a line that alternates two given characters
       for the length of the line. It will also allow to print in the same or in the next line.'''

    if nextLine:
        if (lengthOfLine % 2) == 1:
            print    ((lengthOfLine//2) * (charOne + charTwo)) + charOne
        else:
            print ((lengthOfLine//2) * (charOne + charTwo))
    else:
        if (lengthOfLine % 2) == 1:
            print    (((lengthOfLine//2) * (charOne + charTwo)) + charOne),
        else:
            print (((lengthOfLine//2) * (charOne + charTwo))),
        

def drawthreeDifferentCharLine (charOne, charOneWidth, charTwo, charTwoWidth, charThree, charThreeWidth, nextLine = True):
    '''This function will draw a line with three sections, each section with
       its own character and width. It will also allow to print in the same or in the next line.'''

    if nextLine:
        print (charOne * charOneWidth) + (charTwo * charTwoWidth) + (charThree * charThreeWidth)
    else:
        print (charOne * charOneWidth) + (charTwo * charTwoWidth) + (charThree * charThreeWidth),


def drawGivenRandomLengthLine (randomChar, nextLine = True):
    '''This function will draw a line of a random length, between two given values characters long.
       It will also allow to print in the same or in the next line.'''

    if nextLine:
        print (random.randint(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)) * randomChar
    else:
        print ((random.randint(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE)) * randomChar),


def drawAnknowenRandomLengthLine (minRandomValue, maxRandomValue, randomChar, nextLine = True):
    '''This function will draw a line of a random length, somewhere between two values characters long.
       It will also allow to print in the same or in the next line.'''

    if nextLine:
        print (random.randint(minRandomValue, maxRandomValue)) * randomChar
    else:
        print ((random.randint(minRandomValue, maxRandomValue)) * randomChar),
