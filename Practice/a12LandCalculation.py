''' 
cs1114 

Submission: Land Calculation (Private)

Programmer: Kostaq Papa
Username: kpapa01

Purpose of program: This program will convert the number in squarefeet enterd by the user in acres.
Assumptions: The user will type what I ask for.
Constraints: I dont know what a f*** this mean.

'''

ONE_ACRE = 43560

def enterNoOfSquareFeet ():
    '''This function will ask the user to enter the number of squarefeet.'''

    squareFeet = float (raw_input("Please, enter the area of your land in squarefeet: "))

    return squareFeet

def converToAcres (squareFeet):
    '''This function will conver the number of squarefeet in acres.'''

    acres = squareFeet / ONE_ACRE

    print "The area of your land in acres is: " ,acres

def main():

    squareFeetNumber = enterNoOfSquareFeet ()
    converToAcres (squareFeetNumber)
main ()
