
''' 
cs1114 

Submission: Assignment (Private)

Programmer: Kostaq Papa
Username: kpapa01

Purpose of program: This program will assign different values to only three valiables, first, second, third.
Assumptions: The user will type what I ask for.
Constraints: I dont know what a f*** this mean.

'''

# In this program is required to perform some arithmetic operations using constant variables. Number "2","4","3.14","8" are constant values and they will not change while the program is running. 

FIRST_CONSTANT_NUMBER = 2
SECOND_CONSTAN_NUMBER = 4
THIRD_CONSTANT_NUMBER = 3.14
FORTH_CONSTAN_NUMBER = 8


def enterFirstvaliue ():
    '''This function will ask the user to enter a number.'''

    first_number = float (raw_input ("Pleasa, enter any number you like: "))

    return first_number

def addFirstnumber (first_number):
    '''This function will add a hte FIRST_CONSTANT_NUMBER number to the number entered. The addition value will be stored under the variable named "secodn_number".'''

    second_number = FIRST_CONSTANT_NUMBER + first_number

    print "Did you know that if %.2f is added by 2 the result will be: %.2f" %(first_number, second_number)

    return second_number

def multiplySecondnumber (second_number):
    '''This function will multiply the second_number by SECOND_CONSTAN_NUMBER and will assign this value to the firsr_number variable.'''

    first_number = second_number * SECOND_CONSTAN_NUMBER

    print "Did you know that if %.2f is multiplied by 4 the result would be: %.2f" %(second_number, first_number)


def main ():

    firstValue = enterFirstvaliue ()
    secondValue = addFirstnumber (firstValue)
    multiplySecondnumber (secondValue)

main()
