
#!C:\Users\kpapa01\Desktop\Python\hw\hw01.exe

''' 
cs1114 

Submission: hw01

Programmer: Kostaq Papa
Username: kpapa01

Purpose of program: The purpose of the program is to find the "Three-Times-The-Square-Root" of age.
Assumptions: The user will type what I ask for.
Constraints: I cannot use anything that has not been covered.

'''

import math, random


THE_MULTIPLY_CONSTANT = 3   # In this program is required the "3 times square root of age". Number "3" is a constant value and it will not change while the program is running. It will multyply the square root of user's age, for this reason I stored this variable under "THE_MULTYPLY_CONSTANT" name.


def welcome_users ():
    '''This function will welcome the users.'''
    

    print " WELCOME TO MY PROGRAM!!!\n"



def what_this_program_do ():
    ''' This function will briefly introduce the program to the users and orient them for the next steps.'''


    print " Here, you will find something interesting about your age. \n I am sure you haven't noticed it before. \n Please, answer correctly the below questions.\n"

    

def type_first_and_last_name ():
    '''This function will ask the user to enter his/her first and last name.'''

    
    first_Name =  raw_input ( " Please, enter your first name: " )
    last_Name  =  raw_input ( " Please, enter your last name: "  )

    return first_Name, last_Name



def introduce_myself ( first_Name, last_Name ):
    '''This function will intoduce me with the user.'''


    print " Hello " + first_Name + " " + last_Name + " \n Nice to meet you. My name is Kostaq Papa. I am the designer of this program.\n"
    


def type_age():
    '''This function will ask the user to enter his/her age.'''

    
    theAge = int ( raw_input ( " Please, enter your age: "))

    print "\n"

    return theAge


def character_draw():
    '''This function will draw the required character horizontally. The number of characters will be a random number between minimum range and maximum range.'''

    minimumRange = THE_MULTIPLY_CONSTANT + 10   # The "minimumRange" variable is the minimum value that the random function will have. 
    maximumRange = THE_MULTIPLY_CONSTANT + 20   # The "maximumRange" variable is the maximum value that the random function will have.
    randomCharacter = random.randint(minimumRange, maximumRange)

    print "~" * randomCharacter 

def calculate_three_times_square_root_of_age (theAge):
    '''This function will calculate the "THREE_TIMES_SQUARE_ROOT_OF_AGE of the user.'''

    
    the_three_times_square_root_of_age_is = (math.sqrt(theAge))* THE_MULTIPLY_CONSTANT

    print "\n The 'THREE TIMES SQUARE ROOT OF YOUR AGE' is:%.10f " % the_three_times_square_root_of_age_is

    return  the_three_times_square_root_of_age_is


def say_thankyou_and_goodbye_to_the_users ():
    '''This program will say 'THANKYOU' and 'GOODBYE' to the users.'''


    print " \n\n THANK YOU FOR USING THIS PROGRAM."
    print " GOODBYE AND HAVE A NICE DAY!!!"



def pause_this_program ():
    '''This function will pause the program and will ask the user to exit.'''

    raw_input (" \n\nPlease, press any key to exit...")    



def main ():    

    welcome_users ()

    what_this_program_do ()
    
    firstName, lastName = type_first_and_last_name ()

    introduce_myself (firstName, lastName)

    ageOftheUser = type_age ()    
    
    character_draw ()

    threeTimessquareRootofAge = calculate_three_times_square_root_of_age (ageOftheUser)

    say_thankyou_and_goodbye_to_the_users ()

    pause_this_program ()
    

if __name__ == '__main__':

    main()
