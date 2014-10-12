"""

User Name: kpapa01

Programmer: Kostaq Papa

Purpose of this program: Choose a winner, based an the amount of mouney entered.

Assumption: The user will not type a non integer input. 

"""

def EnterPositiveNumber():
    '''This function will ask the user to enter an intteger, positive number.'''

    positiveNumber = int(raw_input ("Please, enter an integer number(should be positive):"))

    return positiveNumber

def TestPositiveNumber (positiveNumber):
    '''This function will test if the user entered a positive number.'''

    while ( positiveNumber < 0):

        print "You  did not enter a positive integer number."
        print "Please try again."
        
        positiveNumber = int(raw_input ("Please, enter an integer number(should be positive):"))

        print "You entered a correct number."

def main():

    Number = EnterPositiveNumber()
    TestPositiveNumber (Number)
    
main()
