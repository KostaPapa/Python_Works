#!C:\Users\kpapa01\Desktop\Python\hw\hw03\hw04tester.exe

''' 
cs1114 

Submission: hw03
Required Filename: hw04tester.py

Programmer: Kostaq Papa
Username: kpapa01
ID Number : 0412768

Purpose of program: The purpose is to present and orient the user with the program.

'''
EXIT_PROGRAM = 'QUIT'
ONE = '1'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
LINE_SEPARATOR = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'


import linesModule, shapesModule



def displayMenu():
    '''This function will display the menu to the user.'''

    
    print LINE_SEPARATOR
    print "\t>>> WELCOME TO THE DRAWING PROGRAM <<<\n"
    print "-> Please, press 1 to draw a two character box."
    print "-> Please, press 2 to draw a two character triangle."
    print "-> Please, press 3 to draw a three character box."
    print "-> Please, press 4 to draw THE SPECIAL BOX."
    print "-> Please, press 5 to draw THE SPECIAL TRIANGLE."
    print "-> To exit the program, type " + EXIT_PROGRAM + "\n"
    print LINE_SEPARATOR

    userChoice = raw_input ("Please, enter your choice: ")
    
    while (userChoice != EXIT_PROGRAM):
        
        if (userChoice == ONE):
            shapesModule.drawTwoCharBox()

        elif (userChoice == TWO):
            shapesModule.drawTwoCharTriangle()

        elif (userChoice == THREE):
            shapesModule.drawThreeDifferentCharBox()

        elif (userChoice == FOUR):
            shapesModule.drawSpecialBox()

        elif (userChoice == FIVE):
            shapesModule.drawSpecialTriangle()

        else:
            print "The coice you entered is not offered in this program."
            
        userChoice = raw_input ("Please, try another choice: ")

        if (userChoice == EXIT_PROGRAM):
            print "THANK YOU FOR USING THIS PROGRAM. COME TO DRAW AGAIN.(*_^)"
            print "GOODBYE!!!"


def main():

    displayMenu()
    
# are we being executed?
if __name__ == '__main__':
    main()
    
