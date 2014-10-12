#!C:\Users\kpapa01\Desktop\Python\hw\hw03\userInput.exe

''' 
cs1114 

Submission: hw03
Required Filename: userInput.py

Programmer: Kostaq Papa
Username: kpapa01
ID Number : 0412768

Purpose of program: The purpose of this program is to get the user data.

'''

def getSpecialBoxCharAndHeight():
    '''This function will get the height, the inner and the outer characters
       to draw the special box. This funtion will draw the box when the height is
       an odd and greater than 2 integer, and only when the outer and inner character are different.'''

    heightOfSpecialBox = int(raw_input("Please, enter the height of the box: "))
    while ((heightOfSpecialBox % 2) == 0):
        print "The number must be an odd integer."
        heightOfSpecialBox = int(raw_input("Please, enter the height of the box: "))
        
    while ((heightOfSpecialBox) < 3):
        print "Please, enter a number greater than 2."
        heightOfSpecialBox = int(raw_input("Please, enter the height of the box: "))

    outerChar = raw_input ("Please, enter the outer character of the special box: ")
    innerChar = raw_input ("Please, enter the inner character of the special box: ")

    while (outerChar == innerChar):
        print "The first and second characters must be different."
        outerChar = raw_input ("Please, enter the outer character of the special box: ")
        innerChar = raw_input ("Please, enter the inner character of the special box: ")

    favoriteName = raw_input ("Please, enter your favorite name: ")

    return heightOfSpecialBox, outerChar, innerChar, favoriteName


def getTriangleWidth():
    '''This function will get the width for drawing a triangle. It will draw a triangle
       only when the width is greater than 3.'''

    widthOfTriangle = int (raw_input("Enter the width of the triangle: "))

    while (widthOfTriangle < 3):
        print "Sorry. Enter a number larger than 3."        
        widthOfTriangle = int(raw_input("Enter the width of the triangle: "))

    outerChar = raw_input("Please, enter the outer character:")
    innerChar = raw_input("Please, enter the inner character:")

    typeOfTriangle = raw_input("What type of triangle do you want? (type TOP for a top to bottom triangle/type BOTTOM for a bottom to top triangle)")

    return widthOfTriangle, outerChar, innerChar, typeOfTriangle
