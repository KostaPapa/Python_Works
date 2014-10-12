#!C:\Users\kpapa01\Desktop\Python\hw\hw03\shapesModule.exe

''' 
cs1114 

Submission: hw03
Required Filename: shapesModule.py

Programmer: Kostaq Papa
Username: kpapa01
ID Number : 0412768

Purpose of program: The purpose of this program is to make module that draws boxes and triangles.

Assumption: The user will type BOTTOM for drawing a bottom to top triangle.
'''


DRAW_TRIANGLE_TOP_TO_BOTTOM = 'TOP'         # When the user types TOP, the function where the DRAW_TRIANGLE_TOP_TO_BOTTOM global constant is used, will draw a top to bottom triangle.

import linesModule, userInputModule



# This function uses the imported 'drawTwoCharLine' function from the python
# filename 'linesModule.py' to draw a box.
def drawTwoCharBox():
    '''This function will draw a two character box.'''

    for n in range(5):


        linesModule.drawTwoCharLine('X', 'Y', 8)

    print "\n"


# This function uses the imported 'drawTwoCharLine' function from the python
# filename 'linesModule.py' to draw a triangle.
def drawTwoCharTriangle():
    '''This function will draw a two character triangle.'''

    for length in range (0, 7, 1):

        linesModule.drawTwoCharLine('X', 'Y', (length + 1))

    print "\n"


# This function uses the imported 'drawthreeDifferentCharLine' function from the python
# filename 'linesModule.py' to draw a box.        
def drawThreeDifferentCharBox():
    '''This function will draw a box with three different characters.'''

    for length in range (5):

        linesModule.drawthreeDifferentCharLine('X', 4 , '*', 8, '@', 5)

    print "\n"
    

# This function uses the imported 'getSpecialBoxCharAndHeight' function from the python
# filename 'userInputModule.py' to draw a box.
def drawSpecialBox():
    '''This function will draw a box where in the center of it with will be written the user's favorite string.'''


    heightOfSpecialBox, outerChar, innerChar, favoriteName = userInputModule.getSpecialBoxCharAndHeight()

    print (outerChar * (len(favoriteName) + (3 * len(innerChar)) + (3 * len(innerChar)) + (len(outerChar) + len(outerChar))))

    for n in range((heightOfSpecialBox - 3)/2):
        print (outerChar + (innerChar * ((3 * len(innerChar)) + (len(favoriteName)) + (3 * len(innerChar)))) + outerChar)        

    print (outerChar + (innerChar * 3) + favoriteName + (innerChar * 3) + outerChar)

    for n in range((heightOfSpecialBox - 3)/2):
        print (outerChar + (innerChar * ((3 * len(innerChar)) + (len(favoriteName)) + (3 * len(innerChar)))) + outerChar)
    
    print (outerChar * (len(favoriteName) + (3 * len(innerChar)) + (3 * len(innerChar)) + (len(outerChar) + len(outerChar))))


# This function uses the imported 'getTriangleWidth' function from the python
# filename 'userInputModule.py' to draw a triangle.
def drawSpecialTriangle():
    '''This function will draw a two character triangle.'''

    widthOfTriangle, outerChar, innerChar, typeOfTriangle = userInputModule.getTriangleWidth()

        
    if (typeOfTriangle == DRAW_TRIANGLE_TOP_TO_BOTTOM):
        print outerChar
        for n in range(1, widthOfTriangle - 1, 1):
            print outerChar + (innerChar * (n - 1)) + outerChar
        print outerChar * widthOfTriangle

    else:    
        print outerChar * widthOfTriangle
        for n in range (widthOfTriangle - 2, 0, -1):
            print outerChar + (innerChar * (n - 1)) + outerChar
        print outerChar
