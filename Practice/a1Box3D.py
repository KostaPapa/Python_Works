"""

User Name: kpapa01

Programmer: Kostaq Papa

Purpose of this program: This program will print a 3D box with different widths, heigh and length.

Constrains: It will compile from left to right.
 

"""

import os


def draw_the_top_and_the_botton_of_the_rectangle (width,character):
    ''' This function, using 'X' as character, will draw the top and the button of the rectangle. '''

    print width * character

    

def draw_the_left_right_part_and_the_middle_spaces_of_the_rectangle (width, character):
    ''' This function will draw the left - right parts and the middle spaces of the triangle. '''

    print character + ' ' * width + character


def draw_its_length (width, character):

    print character + ' ' * width + character
    print ' ' + character + '        ' + character
    print '  ' + width * character


    
    


def right_side (width,character):

    print 

    
def draw_rectangle (width,character):
    ''' This function will draw a rectangle with 'X' as character.'''
    

    
    draw_the_top_and_the_botton_of_the_rectangle (width,character)
    draw_the_left_right_part_and_the_middle_spaces_of_the_rectangle (width,character)
    draw_the_left_right_part_and_the_middle_spaces_of_the_rectangle (width,character)
    draw_the_left_right_part_and_the_middle_spaces_of_the_rectangle (width,character)
    draw_the_top_and_the_botton_of_the_rectangle (width,character)
    draw_its_length (width, character)





def main ():

    print "Below are the rectangular with 10x5 dimensions. \n\n"


    print "Rectangle number 1.\n"
    draw_rectangle (7,'x')
    print "\n\n"

    print "Rectangle number 2. \n"
    draw_rectangle (8,'x')
    print "\n\n"

    print "Rectangle number 3. \n"
    draw_rectangle (9,'x')
    print "\n\n"

    print "Rectangle number 4. \n"
    draw_rectangle (10,'x')
    print "\n\n"

main ()

os.system ("pause")
