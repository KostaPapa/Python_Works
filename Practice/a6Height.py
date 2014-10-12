

''' 
cs1114 

Submission: Interest Rate (Private)

Programmer: Kostaq Papa
Username: kpapa01

Purpose of program: This program will ask the user to enter his or her height and will display his/her height.
Assumptions: The user will type what I ask for.
Constraints: I dont know what a f*** this mean.

'''

def enterHeight():
    '''This function will ask the user to enter his/her height'''

    height = float (raw_input ("Please enter your height:"))

    return height

def displayHeight(height):
    '''This function will display the height entered by the user.'''

    print "Your height is: %.2f" %height
    
def main ():

    userHeight = enterHeight ()
    displayHeight (userHeight)
    
main ()
