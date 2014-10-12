"""

User Name: kpapa01

Programmer: Kostaq Papa

Purpose of this program: This program will print a box with a certain width and character.

Constrains: It will compile from left to right. The is an integer number.
 

"""

    


def askTheuserToenterCharacter ():
    '''This function will ask the user to enter a character for the box.'''

    character = raw_input ("Please enter a character:")
    
    return character

def askTheuserToenterWidthAndNumberOfBoxes():
    '''This function will ask the user to enter width.'''

    width = int ( raw_input("Please, enter the width of the box: "))
    numberOfboxes = int (raw_input ("Please, enter the number of boxes you wish to draw: "))


    return width, numberOfboxes

def testThewidthAndNumberOfBoxes (width, numberOfboxes):
    '''This function will test if the width is positive.'''

    while (width < 0):

        print "The number entered fot the box width must be positive."
        print "Please try again."

        width = int ( raw_input("Please, enter the width of the box: "))
        print "The number you entered is correct."

    while (numberOfboxes < 0):

        print "The number entered must be positive."
        print "Please try again."

        numberOfboxes = int (raw_input ("Please, enter the number of boxes you wish to draw: "))
        print "The number you entered is correct."


def topAndbottonLineofThebox (width, character):
    '''This function draws the top and the botton line of the box'''

    topAndBotton = (width * character)

    print topAndBotton

def middleSpacesofThebox (width, character):
    ''' the middle line of the box will have a 'width' space. '''
    
    print character + ' ' * width + character


def pressAnykeyToexit():
    '''This function will ask the user to exit.'''

    raw_input ("Please, enter any key to exit....")
    
def main ():
    
    ''' Draws a box with a certain width and characters. Width must be numeric '''

    boxCharacter = askTheuserToenterCharacter()
    boxWidth, boxNumber = askTheuserToenterWidthAndNumberOfBoxes ()

    testThewidthAndNumberOfBoxes(boxWidth, boxNumber)

    topAndbottonLineofThebox (boxWidth, boxCharacter)
    middleSpacesofThebox (boxWidth, boxCharacter)
    middleSpacesofThebox (boxWidth, boxCharacter)
    middleSpacesofThebox (boxWidth, boxCharacter)
    middleSpacesofThebox (boxWidth, boxCharacter)
    topAndbottonLineofThebox (boxWidth, boxCharacter)

    pressAnykeyToexit()
    

main ()
