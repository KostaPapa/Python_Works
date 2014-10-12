
''' 
cs1114 

Submission: Interest Rate (Private)

Programmer: Kostaq Papa
Username: kpapa01

Purpose of program: This program will ask the user to enter his/her favorite color.
Assumptions: The user will type what I ask for.
Constraints: I dont know what a f*** this mean.

'''

def enterFavoritecolor():
    '''This function will ask the usr to enter his/her favorite color.'''

    favorite_color = raw_input ("Please, enter your favorite color: ")

    return favorite_color

def displayFavoritecolor(favorite_color):
    '''This function will display the favorite color the the user entered.'''

    print "Your favorite color is: " , favorite_color

def main():

    userColor = enterFavoritecolor ()
    displayFavoritecolor (userColor)

main()
