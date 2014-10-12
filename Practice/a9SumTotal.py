''' 
cs1114 

Submission: Assignment (Private)

Programmer: Kostaq Papa
Username: kpapa01

Purpose of program: This program will calculate the sum of two constatns and will assign it to a variable named total.
Assumptions: The user will type what I ask for.
Constraints: I dont know what a f*** this mean.

'''

def enterTwoNumbers ():

    firstNumber = float (raw_input ("Please, enter the first number: "))
    secondNumber = float (raw_input ("Please enter the second number: "))

    return firstNumber, secondNumber

def addTwoConst (firstNumber, secondNumber):
    '''This function will add the sum of two numbers enterd by the user.'''

    total = firstNumber + secondNumber

    print "Did you know that the sum of %.3f and %.3f is %.3f. " %(firstNumber, secondNumber, total)

def main():

    numberOne, NumberTwo = enterTwoNumbers ()
    addTwoConst (numberOne, NumberTwo)
main ()
