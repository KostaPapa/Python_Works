#!C:\Users\kpapa01\Desktop\Python\hw\hw01.exe

''' 
cs1114 

Submission: Interest Rate (Private)

Programmer: Kostaq Papa
Username: kpapa01

Purpose of program: The purpose of the program is to find the interest needed to achive the desired amount of money in the future.
Assumptions: The user will type what I ask for.
Constraints: I dont know what a f*** this mean.

'''

import math

def initialAmount ():
    '''This will ask the user to enter the initial amount that he wants to deposit.'''

    initial_amount = float (raw_input ("Please, enter your initial amount: "))

    return initial_amount

def amountDesired ():
    '''This function will ask the user to enter the amount that he desires to have.'''

    desired_amount = float (raw_input ("Please, enter the amount that you desire to have: "))

    return desired_amount

def time ():
    '''This function will ask the user to enter the period of time, in years, that the initial amount of money will stay in bank.'''

    time = float (raw_input ("Please enter the time of investement: "))

    return time

def calculationOfinterestRate (desired_amount, initial_amount, time):
    '''This function will calculate the interest rate needed to achive the desired amount of money.'''

    interest_rate = (pow ((desired_amount / initial_amount), (1/time)))

    print "You should find a bank which has this interest rate: %.6f " %interest_rate
    
def main ():

    presentAmount = initialAmount ()
    futureAmount = amountDesired ()
    timePeriod = time ()
    calculationOfinterestRate (presentAmount, futureAmount, timePeriod)

main ()
